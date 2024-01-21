from django.contrib import admin
from . import forms 

class PillowAdmin(admin.ModelAdmin):
    list_display = [field.name for field in forms.Pillow._meta.get_fields()] 
    search_fields=["name"]
    form = forms.PillowForm

admin.site.register(forms.Pillow, PillowAdmin)

class SeatCushionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in forms.SeatCushion._meta.get_fields()] 
    search_fields=["name"]
    form = forms.SeatCushionForm

admin.site.register(forms.SeatCushion, SeatCushionAdmin)

class RugAdmin(admin.ModelAdmin):
    list_display = [field.name for field in forms.Rug._meta.get_fields()] 
    search_fields=["name"]
    form = forms.RugForm

admin.site.register(forms.Rug, RugAdmin)

class WallArtAdmin(admin.ModelAdmin):
    list_display = [field.name for field in forms.WallArt._meta.get_fields()] 
    search_fields=["name"]
    form = forms.WallArtForm

admin.site.register(forms.WallArt, WallArtAdmin)