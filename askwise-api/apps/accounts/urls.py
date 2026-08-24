from django.urls import path, include

from apps.accounts.views import GoogleLoginView, GoogleOAuthJWTCallbackView, TokenRefreshAPIView

urlpatterns = [
    path("google/login/", GoogleLoginView.as_view(), name="google_login"),
    path("", include("allauth.urls")),
    path("google/callback/", GoogleOAuthJWTCallbackView.as_view(), name="google_callback"),
    path("token/refresh/", TokenRefreshAPIView.as_view(), name="token_refresh"),
]