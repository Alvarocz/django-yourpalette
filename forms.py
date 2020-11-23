from django import forms

from .models import ColorPalette
from .fields import HexColorFormField
from .utils import darken, lighten


class ColorPaletteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields.keys():
            default = ColorPalette._meta.get_field(name).default
            self.fields[name] = HexColorFormField(
                initial=default,
                dark=darken(default),
                light=lighten(default)
            )

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

