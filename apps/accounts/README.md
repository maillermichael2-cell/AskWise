# AskWise Authentication Architecture

This document describes the authentication architecture used by AskWise.

## Overview

AskWise uses the following technologies for authentication:

- Django
- Django REST Framework
- Django Allauth
- Google OAuth 2.0
- Simple JWT
- PostgreSQL
- Stateless JWT Authentication

The philosophy behind the implementation is simple:

> Let Allauth handle OAuth.
>
> Let AskWise handle application authentication.

---

## Authentication Flow

```text
Client
   │
   ▼
GET /api/v1/auth/google/login/
   │
   ▼
Google OAuth
   │
   ▼
Django Allauth
   │
   ▼
User authenticated
   │
   ▼
Redirect
/api/v1/auth/token/login/
   │
   ▼
AuthService.login(user)
   │
   ▼
JWTService.build_auth_response(user)
   │
   ▼
JSON Response
```

---

## Design Principles

### Allauth Responsibilities

- Google Authentication
- User Creation
- Social Account Linking
- Session Management
- Existing User Login

### AskWise Responsibilities

- JWT Generation
- Profile Creation
- User Synchronization
- Authentication Response
- Frontend Integration

---

## Project Structure

```text
apps/
└── accounts/
    ├── adapters.py
    ├── views.py
    ├── urls.py
    ├── models.py
    │
    └── services/
        ├── auth_service.py
        ├── jwt_service.py
        └── profile_service.py
```

---

## Authentication Services

### JWTService

Responsible for:

- Access Token Generation
- Refresh Token Generation
- Building Authentication Responses

```python
class JWTService:
    @staticmethod
    def generate_tokens(user):
        ...

    @staticmethod
    def build_auth_response(user):
        ...
```

Example:

```json
{
    "access": "<JWT_ACCESS_TOKEN>",
    "refresh": "<JWT_REFRESH_TOKEN>",
    "user": {
        "id": "1",
        "email": "askwise@gmail.com",
        "display_name": "AskWise",
        "avatar": "",
        "account_type": null
    }
}
```

---

### ProfileService

Responsible for:

- Ensuring Profile Exists
- Synchronizing Profile Information
- Future Avatar Synchronization

```python
class ProfileService:

    @staticmethod
    def ensure_profile(user):
        ...
```

---

### AuthService

Responsible for orchestrating the login flow.

```python
class AuthService:

    @staticmethod
    def login(user):
        ...
```

Responsibilities:

- Ensure profile exists.
- Update `last_login`.
- Generate JWT tokens.
- Return authentication response.

---

## Views

### GoogleLoginView

Starts the Google OAuth flow.

```python
GET /api/v1/auth/google/login/
```

Implementation:

```python
class GoogleLoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        adapter = get_social_adapter(request)
        provider = adapter.get_provider(
            request,
            provider="google",
        )

        return provider.redirect(
            request,
            process=AuthProcess.LOGIN,
        )
```

---

### TokenLoginView

Returns JWT tokens after successful authentication.

```python
GET /api/v1/auth/token/login/
```

Implementation:

```python
class TokenLoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):

        if not request.user.is_authenticated:
            return Response(
                {
                    "success": False,
                    "message": "Google authentication failed."
                },
                status=401,
            )

        return Response(
            {
                "success": True,
                "message": "Login successful.",
                **AuthService.login(request.user),
            }
        )
```

---

## URL Configuration

```python
urlpatterns = [
    path(
        "google/login/",
        GoogleLoginView.as_view(),
        name="google_login",
    ),

    path(
        "token/login/",
        TokenLoginView.as_view(),
        name="token_login",
    ),

    path(
        "",
        include("allauth.urls"),
    ),
]
```

---

## Settings

### Redirect URL

```python
LOGIN_REDIRECT_URL = "/api/v1/auth/token/login/"
```

### Social Account Adapter

```python
SOCIALACCOUNT_ADAPTER = (
    "apps.accounts.adapters.SocialAccountAdapter"
)
```

### JWT

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}
```

---

## Complete Authentication Flow

### Existing User

```text
Google Login
      │
      ▼
Allauth
      │
      ▼
Find Existing User
      │
      ▼
Create Session
      │
      ▼
TokenLoginView
      │
      ▼
JWTService
      │
      ▼
JSON Response
```

---

### New User

```text
Google Login
      │
      ▼
Allauth
      │
      ▼
Create User
      │
      ▼
Create SocialAccount
      │
      ▼
TokenLoginView
      │
      ▼
ProfileService
      │
      ▼
JWTService
      │
      ▼
JSON Response
```

---

## Example Response

```json
{
    "success": true,
    "message": "Login successful.",
    "access": "eyJhbGciOi...",
    "refresh": "eyJhbGciOi...",
    "user": {
        "id": "1",
        "email": "askwise@gmail.com",
        "first_name": "",
        "last_name": "",
        "display_name": "",
        "avatar": "",
        "account_type": null
    }
}
```

---

## Future Improvements

- GitHub OAuth
- Apple OAuth
- Microsoft OAuth
- One-Time Authorization Codes
- Token Blacklisting
- Multi-Factor Authentication
- Session Management
- Device Tracking
- Refresh Token Rotation

---

## Architectural Advantages

1. Stateless Authentication.
2. Provider Agnostic.
3. Easily Extensible.
4. Simple Service Layer.
5. Frontend Friendly.
6. Mobile Friendly.
7. OAuth Logic Delegated to Allauth.
8. Clean Separation of Concerns.

---

## Final Architecture

```text
                     Google
                        │
                        ▼
                 Django Allauth
                        │
                        ▼
                 AuthService
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
      ProfileService         JWTService
             │                     │
             └──────────┬──────────┘
                        ▼
                  JSON Response
```

---

## Philosophy

> Allauth proves identity.
>
> AskWise authenticates the application user.
>
> JWT secures the API.
>
> Services orchestrate the business logic.
>
> The frontend consumes a simple JSON response.