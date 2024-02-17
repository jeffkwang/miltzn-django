from django.shortcuts import render
import datetime as dt
import json

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.db.transaction import atomic, non_atomic_requests
from square.utilities.webhooks_helper import is_valid_webhook_event_signature
from django.utils import timezone
from django.http import HttpResponse, HttpResponseForbidden

from django.conf import settings
from .models import WebhookMessage

SIGNATURE_KEY = ""
NOTIFICATION_URL = ""

@csrf_exempt
@require_POST
@non_atomic_requests
def square_webhook(request):
    length = int(request.headers.get('content-length', 0))
    body = request.rfile.read(length).decode('utf-8')
    square_signature = request.headers.get('x-square-hmacsha256-signature')
    is_from_square = is_valid_webhook_event_signature(body,
                                                          square_signature,
                                                          SIGNATURE_KEY,
                                                          NOTIFICATION_URL)
    if is_from_square:
            # Signature is valid. Return 200 OK.
            request.send_response(200)
            payload = json.loads(request.body)
            WebhookMessage.objects.create(
                received_at=timezone.now(),
                payload=body,
            )
            print("Request body: {}".format(body))
    else:
            # Signature is invalid. Return 403 Forbidden.
            request.send_response(403)

    request.end_headers()

    # AcmeWebhookMessage.objects.filter(
    #     received_at__lte=timezone.now() - dt.timedelta(days=7)
    # ).delete()

    return HttpResponse("Message received okay.", content_type="text/plain")