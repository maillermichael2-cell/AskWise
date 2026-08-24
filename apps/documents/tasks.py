from celery import shared_task 
from django.core.cache import cache
from .models import KnowledgeDocument
from .utils import extract_text_from_file
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def extract_document_content(self, document_id):
    lock_key = f"extract_lock:{document_id}"

    # Acquire a lock so only one worker can process this document at a time.
    # nx=True means "only set if it doesn't already exist" — atomic in Redis.
    lock_acquired = cache.add(lock_key, "locked", timeout=300)  # 5 min safety timeout

    if not lock_acquired:
        logger.info(f"Extraction already in progress for document {document_id}, skipping.")
        return

    try:
        doc = KnowledgeDocument.objects.get(id=document_id)

        # Idempotency check: skip if already completed
        if doc.status == KnowledgeDocument.STATUS_COMPLETED:
            logger.info(f"Document {document_id} already processed, skipping.")
            return

        doc.status = KnowledgeDocument.STATUS_PROCESSING
        doc.save(update_fields=['status'])

        doc.file.open('rb')
        extracted_text = extract_text_from_file(doc.file, doc.file_name)
        doc.file.close()

        KnowledgeDocument.objects.filter(pk=doc.pk).update(
            content=extracted_text,
            status=KnowledgeDocument.STATUS_COMPLETED,
        )
        logger.info(f"Content extracted for document {document_id} ({len(extracted_text)} chars)")

    except KnowledgeDocument.DoesNotExist:
        logger.error(f"Document {document_id} not found for content extraction")

    except Exception as exc:
        logger.error(f"Failed to extract content for document {document_id}: {exc}")
        KnowledgeDocument.objects.filter(pk=document_id).update(status=KnowledgeDocument.STATUS_FAILED)
        raise self.retry(exc=exc)

    finally:
        cache.delete(lock_key)