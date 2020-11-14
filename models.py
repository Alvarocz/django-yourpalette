from django.db import models

from .fields import HexColorField


class ColorPalette(models.Model):
    white = HexColorField()
    black = HexColorField(default="#000000")
    gray = HexColorField(default="#FAFAFA")
    red = HexColorField(default="#f14242")
    green = HexColorField(default="#2dce4c")
    blue = HexColorField(default="#4ca3bb")
    orange = HexColorField(default="#fd914b")
    yellow = HexColorField(default="#fcff68")
    purple = HexColorField(default="#966ba6")
    fuchsia = HexColorField(default="#fe44ae")
    extra1 = HexColorField(default="#515b6b")
    extra2 = HexColorField(default="#6b5167")
    extra3 = HexColorField(default="#0cfc82")
    extra4 = HexColorField(default="#0cfc4c")
    extra5 = HexColorField(default="#fc0c4c")
    light_factor = models.IntegerField()
    dark_factor = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        for field in self._meta.fields:
            attr = getattr(self, field.name)
            print(attr)

        super().save(*args, **kwargs)
