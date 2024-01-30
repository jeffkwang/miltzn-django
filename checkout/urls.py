from django.urls import path, include

from . import views

app_name="checkout"

urlpatterns = [
    path("", views.checkout_view, name="checkout"),
]