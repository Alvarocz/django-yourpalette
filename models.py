from django.db import models

from .fields import HexColorField


class ColorPalette(models.Model):
    white = HexColorField()
    black = HexColorField(default="#000000")
    light_gray = HexColorField(default="#F0F0F0")
    gray = HexColorField(default="#FAFAFA")
    dark_gray = HexColorField(default="#222222")
    light_blue = HexColorField(default="#b6e1ed")
    blue = HexColorField(default="#4ca3bb")
    dark_blue = HexColorField(default="#12647a")
    purple = HexColorField(default="#966ba6")
    fuchsia = HexColorField(default="#fe44ae")
    light_green = HexColorField(default="#97f4a9")
    green = HexColorField(default="#2dce4c")
    dark_green = HexColorField(default="#248737")
    light_red = HexColorField(default="#ec9898")
    red = HexColorField(default="#f14242")
    dark_red = HexColorField(default="#782121")
    orange = HexColorField(default="#fd914b")
    yellow = HexColorField(default="#fcff68")
    extra1 = HexColorField(default="#515b6b")
    extra2 = HexColorField(default="#6b5167")
    extra3 = HexColorField(default="#0cfc82")
    extra4 = HexColorField(default="#0cfc4c")
    crated_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
