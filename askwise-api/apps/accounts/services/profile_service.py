from apps.accounts.models import Profile


class ProfileService:

    @staticmethod
    def ensure_profile(user):
        profile, _ = Profile.objects.get_or_create(
            user=user,
            defaults={
                "display_name": user.get_full_name() or user.email.split("@")[0],
            },
        )

        return profile