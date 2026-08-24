from django.test import TestCase
from rest_framework.test import APIClient

from apps.accounts.models import User


class OrganizationAPITests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="owner@example.com", password="password123")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_can_create_and_list_organizations(self):
        payload = {
            "name": "AskWise Labs",
            "description": "AI workspace for support teams",
        }

        create_response = self.client.post("/api/v1/org/organizations/", payload, format="json")
        self.assertEqual(create_response.status_code, 201)
        self.assertEqual(create_response.json()["name"], "AskWise Labs")
        self.assertEqual(create_response.json()["slug"], "askwise-labs")

        list_response = self.client.get("/api/v1/org/organizations/")
        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(len(list_response.json()), 1)
        self.assertEqual(list_response.json()[0]["name"], "AskWise Labs")
