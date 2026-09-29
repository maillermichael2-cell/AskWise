import os
from django.db import models
from django.core.exceptions import ValidationError
from pgvector.django import VectorField, HnswIndex

def validate_file_type(value):
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.pdf', '.docx', '.doc', '.txt', '.md']
    if ext not in valid_extensions:
        raise ValidationError('Unsupported format. Only PDF, DOCX, TXT, and MD are allowed.')

class KnowledgeDocument(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_PROCESSING = 'processing'
    STATUS_COMPLETED = 'completed'
    STATUS_FAILED = 'failed'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_PROCESSING, 'Processing'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_FAILED, 'Failed'),
    ]
    # Dynamically reference the Organization model from your other app
    organization = models.ForeignKey('organizations.Organization', on_delete=models.CASCADE, related_name="documents")
    file = models.FileField(upload_to="kb_documents/", validators=[validate_file_type])
    file_name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return f"{self.file_name or self.file.name} - Org ID: {self.organization_id}"

    def save(self, *args, **kwargs):
        if not self.file_name and self.file:
            self.file_name = os.path.basename(self.file.name)
        super().save(*args, **kwargs)



class DocumentChunk(models.Model):
    document = models.ForeignKey(KnowledgeDocument, on_delete=models.CASCADE, related_name="chunks")
    chunk_index = models.IntegerField()
    text = models.TextField()
    embedding = VectorField(dimensions=384)  # all-MiniLM-L6-v2 output size
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["chunk_index"]
        indexes = [
            HnswIndex(
                name="chunk_embedding_hnsw_idx",
                fields=["embedding"],
                m=16,
                ef_construction=64,
                opclasses=["vector_cosine_ops"],
            )
        ]