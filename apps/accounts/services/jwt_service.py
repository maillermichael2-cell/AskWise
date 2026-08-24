from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed


class JWTService:
    @staticmethod
    def generate_tokens(user):
        """
        Generate JWT access and refresh tokens for a user.
        """
        refresh = RefreshToken.for_user(user)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }

    @staticmethod
    def build_auth_response(user):
        tokens = JWTService.generate_tokens(user)

        profile = getattr(user, "profile", None)

        return {
            "access": tokens["access"],
            "refresh": tokens["refresh"],
            "user": {
                "id": str(user.id),
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "display_name": profile.display_name if profile else "",
                "avatar": profile.avatar if profile else "",
                "account_type": profile.account_type if profile else None,
            },
        }
    @staticmethod
    def refresh_access_token(refresh_token:str) -> str:
        """
            generates a new access token from a valid refresh token
        """
        try:
            refresh = RefreshToken(refresh_token)
            return str(refresh.access_token)
        except Exception:
            raise AuthenticationFailed("Invalid or expired refresh token.")