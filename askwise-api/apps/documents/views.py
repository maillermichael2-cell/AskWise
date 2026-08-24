from rest_framework import generics, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import KnowledgeDocument
from .serializers import KnowledgeDocumentSerializer
from .tasks import extract_document_content

class DocumentUploadView(generics.ListCreateAPIView):
    serializer_class = KnowledgeDocumentSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        # Only show files belonging to organizations owned by the logged-in user
        return KnowledgeDocument.objects.filter(organization__owner=self.request.user)

    def perform_create(self, serializer):
        org = serializer.validated_data.get('organization')
        
        # Security Boundary: Confirm user owns the target organization
        if org.owner != self.request.user:
            raise exceptions.PermissionDenied("You do not have permission to upload files here.")
            
        document = serializer.save()
        extract_document_content.delay(document.id)
