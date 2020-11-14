from django import forms
from django.forms.utils import flatatt
from django.forms.widets import get_default_renderer
from django.utils.encondig import force_str
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe


class HexColorWidget(forms.TextArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        if renderer is None:
            renderer = get_default_renderer()
        if value is None:
            value = ""
        final_attrs = self.build_attrs(self.attrs, attrs, name=name)
        
        return mark_safe(
            renderer.render(
                'yourtemplate/widget.html',
                {
                    'type': 'color',
                    'value': conditional_escape(force_str(value)),
                    'class': 'color-input',
                    'id': 'id_'+name,
                    'final_attrs': flatatt(final_attrs),
                }
            )
        )
