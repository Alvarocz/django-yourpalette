from django import forms

from .models import ColorPalette
from .widgets import HexColorWidget


class ColorPaletteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.initial = ColorPalette._meta.get_field(name).default
            field.widget = HexColorWidget()

    class Meta:
        model = ColorPalette
        fields = [
            'white',
            'black',
            'gray',
            'red',
            'green',
            'blue',
            'orange',
            'yellow',
            'purple',
            'fuchsia',
            'extra1',
            'extra2',
            'extra3',
            'extra4',
            'extra5',
            'light_factor',
            'dark_factor'
        ]

