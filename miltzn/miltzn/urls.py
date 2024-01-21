"""
URL configuration for miltzn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from products import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)  
router.register(r'pillows', views.PillowViewSet)
router.register(r'seatcushions', views.SeatCushionViewSet)
router.register(r'rugs', views.RugViewSet)
router.register(r'wallart', views.WallArtViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]

urlpatterns += router.urls