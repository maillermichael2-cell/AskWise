from django.urls import path, include


urlpatterns = [
    path("auth/", include("apps.accounts.urls")),
    path("org/", include("apps.organizations.urls")),
    path("documents/", include("apps.documents.urls")),
    path("chat/", include("apps.conversations.urls")),
    path("ai/", include("apps.ai.urls")),
    path('common/', include('apps.common.urls')),
]