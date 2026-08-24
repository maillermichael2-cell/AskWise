from django.utils import timezone

from .jwt_service import JWTService
from .profile_service import ProfileService


class AuthService:
    @staticmethod
    def login(user):
        """
        Complete the login process for an authenticated user.
        """

        # Ensure the user has a profile
        ProfileService.ensure_profile(user)

        # Update last login
        user.last_login = timezone.now()
        user.save(update_fields=["last_login"])

        # Return JWT + user payload
        return JWTService.build_auth_response(user)