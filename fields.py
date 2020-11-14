from __future__ import absolute_import

from django import forms
from django.db import models


class HexColorField(models.CharField):
    description = "Field used to store hex color codes"
    def __init__(self, *args, **kwargs):
        self.dark = "#f0f0f0"
        self.light = "#f0f0f0"
        kwargs['default'] = "#FFFFFF"
        kwargs['max_length'] = 7
        super().__init__(*args, **kwargs)


class HexColorFormField(forms.fields.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)