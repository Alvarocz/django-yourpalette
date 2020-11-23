from django import forms

from .models import ColorPalette
from .fields import HexColorFormField
from .utils import darken, lighten


class ColorPaletteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dark_factor = ColorPalette._meta.get_field('dark_factor').default
        light_factor = ColorPalette._meta.get_field('light_factor').default
        for name in self.fields.keys():
            default = ColorPalette._meta.get_field(name).default
            if type(default) is int:
                break
            self.fields[name] = HexColorFormField(
                initial=default,
                dark=darken(default, dark_factor),
                light=lighten(default, light_factor)
            )
            print('')
            print(self.fields[name].dark)
            print(self.fields[name].initial)
            print(self.fields[name].light)

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

