import datetime as dt
from http import HTTPStatus

from django.test import Client, override_settings, TestCase
from django.utils import timezone

from .models import WebhookMessage

@override_settings(SIGNATURE_KEY="abc123")
class WebhookMessageTests(TestCase):
    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)
    
    def test_bad_method(self):
        response = self.client.get("/webhooks/square")
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED

    def test_missing_token(self):
        response = self.client.post(
            "/webhooks/square",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN
        assert (
            response.content.decode() == "Incorrect token in Square-Webhook-Token header."
        )