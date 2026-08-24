import requests
from django.conf import settings



class GoogleService:
    
    TOKEN_URL = "https://oauth2.googleapis.com/token"

    @staticmethod
    def exchange_code(code, redirect_uri=None):
        response = requests.post(
            GoogleService.TOKEN_URL,
            data={
                "code": code,
                "client_id": settings.GOOGLE_CLIENT_ID,
                "client_secret": settings.GOOGLE_CLIENT_SECRET,
                "redirect_uri": redirect_uri or settings.GOOGLE_REDIRECT_URI,
                "grant_type": "authorization_code",
            },
        )
        response.raise_for_status()
        return response.json()

    USERINFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"

    @staticmethod
    def get_user_info(access_token):
        response = requests.get(
            GoogleService.USERINFO_URL,
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )
        response.raise_for_status()
        return response.json()