from types import SimpleNamespace

from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import RequestFactory, TestCase

from apps.accounts.models import Profile
from apps.accounts.services import JWTService, OAuthService
from apps.accounts.views import GoogleLoginView


class JWTServiceTests(TestCase):
    def test_build_auth_response_includes_tokens_and_user_profile(self):
        user = get_user_model().objects.create_user(email="test@example.com", password="secret123")
        profile = user.profile
        profile.display_name = "Jane Doe"
        profile.avatar = "https://example.com/avatar.png"
        profile.save()

        response = JWTService.build_auth_response(user)

        self.assertIn("access", response)
        self.assertIn("refresh", response)
        self.assertEqual(response["user"]["email"], user.email)
        self.assertEqual(response["user"]["display_name"], "Jane Doe")
        self.assertEqual(response["user"]["id"], user.id)
        self.assertTrue(Profile.objects.filter(user=user).exists())


class GoogleLoginViewTests(TestCase):
    def test_google_login_redirects_to_google_authorization_url(self):
        request = RequestFactory().get("/api/v1/auth/google/login/")
        request.session = {}

        response = GoogleLoginView.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertIn("accounts.google.com", response["Location"])


class OAuthServiceTests(TestCase):
    def test_get_or_create_user_recovers_when_social_save_hits_duplicate_email(self):
        existing_user = get_user_model().objects.create_user(email="existing@example.com", password="secret123")

        class FakeSocialLogin:
            def __init__(self, user):
                self.account = SimpleNamespace(provider="google", uid="123456", extra_data={"email": existing_user.email})
                self.email_addresses = []
                self.user = user
                self.lookup_calls = 0
                self.saved = []

            def lookup(self):
                self.lookup_calls += 1

            def save(self, *args, **kwargs):
                self.saved.append((args, kwargs))
                raise IntegrityError("UNIQUE constraint failed: accounts_user.email")

        sociallogin = FakeSocialLogin(get_user_model()(email="existing@example.com"))

        user = OAuthService.get_or_create_user(sociallogin)

        self.assertEqual(user, existing_user)
        self.assertEqual(user.email, existing_user.email)
        self.assertEqual(sociallogin.user, existing_user)
