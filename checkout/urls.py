from django.urls import path, include

from . import views

app_name="checkout"

urlpatterns = [
    path("checkout/", views.checkout_view),
]