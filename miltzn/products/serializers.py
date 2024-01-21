from .models import Product, Pillow, SeatCushion, Rug, WallArt
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class PillowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pillow
        fields = '__all__'

class SeatCushionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatCushion
        fields = '__all__'

class RugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rug
        fields = '__all__'

class WallArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = WallArt
        fields = '__all__'


