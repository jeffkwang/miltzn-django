from django.urls import path, include

from . import views

app_name="products"

urlpatterns = [
    path("products/", views.getCatalogItemsFromSquare, name="products"),
    path("products/<str:name>/", views.getItemDetails, name="details"),
]