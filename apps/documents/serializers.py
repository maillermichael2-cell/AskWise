from rest_framework import serializers
from .models import KnowledgeDocument

class KnowledgeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeDocument
        fields = ["id", "organization", "file", "file_name", "uploaded_at"]
        read_only_fields = ["id", "file_name", "uploaded_at"]
