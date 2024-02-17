from django.urls import path, include

from . import views

app_name="notifications"

urlpatterns = [
    path("webhooks/square", views.square_webhook, name="square-webhook-url"),
]