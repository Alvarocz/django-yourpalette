from django import forms

from .models import ColorPalette
from .widgets import HexColorWidget


class ColorPaletteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name] = HexColorFormField(
                initial=ColorPalette._meta.get_field(name).default)

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

