from django.urls import path
from .views import csrf, ping

urlpatterns = [
    path('csrf/', csrf, name='csrf'),
    path('ping/', ping, name='ping')
]
