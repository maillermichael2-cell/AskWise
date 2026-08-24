from django.contrib.auth import get_user_model


User = get_user_model()


class UserService:
    @staticmethod
    def get_or_create_google_user(data):
        email = data["email"]
        user, _=User.objects.get_or_create(
            email=email,
            defaults={
                "first_name":data.get("given_name", ""),
                "last_name":data.get("family_name", ""),
            }
        )
        return user