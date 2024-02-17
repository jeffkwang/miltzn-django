from django.contrib import admin
from . import forms 

class PillowAdmin(admin.ModelAdmin):
    list_display = ['name', 'subtitle', 'slug', 'description', 'price', 'color', 'stock_qty', 'active', 'created_at']
    search_fields=["name"]
    form = forms.PillowForm

admin.site.register(forms.Pillow, PillowAdmin)

class SeatCushionAdmin(admin.ModelAdmin):
    list_display = ['name', 'subtitle', 'slug', 'description', 'price', 'color', 'stock_qty', 'active', 'created_at']
    search_fields=["name"]
    form = forms.SeatCushionForm

admin.site.register(forms.SeatCushion, SeatCushionAdmin)

class RugAdmin(admin.ModelAdmin):
    list_display = ['name', 'subtitle', 'slug', 'description', 'price', 'color', 'stock_qty', 'active', 'created_at']
    search_fields=["name"]
    form = forms.RugForm

admin.site.register(forms.Rug, RugAdmin)

class WallArtAdmin(admin.ModelAdmin):
    list_display = ['name', 'subtitle', 'slug', 'description', 'price', 'color', 'stock_qty', 'active', 'created_at']
    search_fields=["name"]
    form = forms.WallArtForm

admin.site.register(forms.WallArt, WallArtAdmin)