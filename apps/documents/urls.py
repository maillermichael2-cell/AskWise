# knowledge_base/urls.py
from django.urls import path
from .views import DocumentUploadView

urlpatterns = [
    path('upload/', DocumentUploadView.as_view(), name='kb-document-upload'),
]
