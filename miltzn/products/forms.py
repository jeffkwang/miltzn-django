from django.forms import modelform_factory
from .models import Pillow, SeatCushion, Rug, WallArt

PillowForm = modelform_factory(Pillow, fields="__all__")
SeatCushionForm = modelform_factory(SeatCushion, fields="__all__")
RugForm = modelform_factory(Rug, fields="__all__")
WallArtForm = modelform_factory(WallArt, fields="__all__")