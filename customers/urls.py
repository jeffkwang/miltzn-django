from django.urls import path

from . import views

app_name="customers"

urlpatterns = [
    path("new-customer", views.customers_view, name="new-customer"),
    path("check-customer", views.customerExists, name="check-customer"),
    path("update-customer", views.update_customer_view, name="update-customer"),
]