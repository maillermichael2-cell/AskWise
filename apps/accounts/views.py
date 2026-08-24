from __future__ import annotations

from allauth.socialaccount.adapter import get_adapter as get_social_adapter
from allauth.socialaccount.internal import statekit
from allauth.socialaccount.providers.base.constants import AuthProcess
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.utils import get_request_param
from django.conf import settings
from django.urls import reverse
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .services.jwt_service import JWTService
from apps.accounts.services.google_service import GoogleService
from apps.accounts.services.user_service import UserService
from apps.accounts.services.auth_service import AuthService



class GoogleLoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        adapter = get_social_adapter(request)
        provider = adapter.get_provider(request, provider="google")
        return provider.redirect(request, process=AuthProcess.LOGIN)



class GoogleOAuthJWTCallbackView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        code = request.GET.get('code')
        redirect_uri = request.build_absolute_uri(reverse("google_callback"))
        token_data = GoogleService.exchange_code(code, redirect_uri=redirect_uri)
        user_data = GoogleService.get_user_info(token_data["access_token"])
        user = UserService.get_or_create_google_user(user_data)
        # return Response(AuthService.login(user))
        data = AuthService.login(user)

        response = Response({
            "access": data['access'],
            "user": data["user"],
        })

        response.set_cookie(
            key="refresh_token",
            value=data["refresh"],
            httponly=True,
            secure=False,
            samesite="Lax",
            max_age=60 * 60 * 24 * 7,
        )
        return response


class TokenRefreshAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token") # get the already cookied resfresh token

        if not refresh_token:
            return Response(
                {"message": "Refresh token not found."},            # if the resfresh token is invalid or its been tampered with it returns an error message.
                status=status.HTTP_401_UNAUTHORIZED,
            ) 
        access = JWTService.refresh_access_token(refresh_token)

        return Response({
            "access": access
        })
