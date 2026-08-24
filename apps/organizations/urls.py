from django.urls import path

from .views import OrganizationDetailView, OrganizationListCreateView, authTest

urlpatterns = [
    path('test2/', authTest.as_view(), name='auth-test'),
    path('organizations/', OrganizationListCreateView.as_view(), name='organization-list-create'),
    path('organizations/<int:pk>/', OrganizationDetailView.as_view(), name='organization-detail'),
]