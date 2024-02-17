from django.test import Client, TestCase
from http import HTTPStatus
import json

class CustomerEndpointTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_bad_method(self):
        data = {'email': 'test@example.com'}  # Provide a valid email address
        response = self.client.post("/check-customer", data=json.dumps(data), content_type='application/json')
        assert response.status_code == 200