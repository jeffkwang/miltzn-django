from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from rest_framework.response import Response

from django.shortcuts import render, get_object_or_404
from products.models import Product, Pillow, Rug, WallArt, SeatCushion
from rest_framework import permissions, viewsets

from products.serializers import ProductSerializer, PillowSerializer, RugSerializer, WallArtSerializer, SeatCushionSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows products to be viewed.
    """

    queryset = Product.objects.all().order_by('-created_at')  # Specify the queryset attribute
    lookup_field = 'slug'

    # With cookie: cache requested url for each user for 2 hours
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        serializer_class = ProductSerializer(self.queryset, many=True)
        return Response(serializer_class.data)
    
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, slug=None):
        product = get_object_or_404(self.queryset, slug=slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class PillowViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows pillows to be viewed.
    """
    queryset = Pillow.objects.all().order_by('-created_at')
    lookup_field = 'slug'

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        serializer=PillowSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, slug=None):
        product=get_object_or_404(self.queryset, slug=slug)
        serializer=PillowSerializer(product)
        return Response(serializer.data)

class WallArtViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows wall art to be viewed.
    """
    queryset = WallArt.objects.all().order_by('-created_at')
    lookup_field = 'slug'

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        serializer=WallArtSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, slug=None):
        product=get_object_or_404(self.queryset, slug=slug)
        serializer=WallArtSerializer(product)
        return Response(serializer.data)

class SeatCushionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows seat cushions to be viewed.
    """
    queryset = SeatCushion.objects.all().order_by('-created_at')
    lookup_field = 'slug'

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        serializer=SeatCushionSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, slug=None):
        product=get_object_or_404(self.queryset, slug=slug)
        serializer=SeatCushionSerializer(product)
        return Response(serializer.data)

class RugViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows rugs to be viewed.
    """
    queryset = Rug.objects.all().order_by('-created_at')
    lookup_field = 'slug'

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        serializer=RugSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, slug=None):
        product=get_object_or_404(self.queryset, slug=slug)
        serializer=RugSerializer(product)
        return Response(serializer.data)
