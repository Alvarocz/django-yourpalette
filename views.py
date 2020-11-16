from django.views.generic import ListView
from django.views.generic.base import ContextMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import ColorPalette
from .forms import ColorPaletteForm


class YourPaletteMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(settings, 'YOURPALETTE_BASE_TEMPLATE'):
            context['base_template'] = settings.YOURPALETTE_BASE_TEMPLATE
        else:
            context['base_template'] = 'yourtemplate/base/base.html'
        return context


class ColorPaletteListView(ListView, YourPaletteMixin):
    queryset = ColorPalette.objects.order_by('created_at')
    template_name = 'yourpalette/index.pug'
    model = ColorPalette


class ColorPaletteDetailView(DetailView, YourPaletteMixin):
    model = ColorPalette
    template_name = 'yourpalette/detail.pug'


class ColorPaletteCreateView(LoginRequiredMixin, YourPaletteMixin, CreateView):
    model = ColorPalette
    template_name = 'yourpalette/form.pug'
    form_class = ColorPaletteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'new'
        return context


class ColorPaletteUpdateView(LoginRequiredMixin, YourPaletteMixin, UpdateView):
    model = ColorPalette
    template_name = 'yourpalette/form.pug'
    form_class = ColorPaletteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'edit'
        return context


class ColorPaletteDeleteView(LoginRequiredMixin, YourPaletteMixin, DeleteView):
    model = ColorPalette
    success_url = reverse_lazy('yourpalette')

    def get(self, request, *args, **kwargs):
        try:
            object = ColorPalette.objects.get(pk=kwargs['pk'])
            return render(request, 'yourpalette/confirm_delete.html',
                          context={'object': object})
        except ColorPalette.DoesNotExist:
            return render(request, 'yourpalette/errors/404.html', status=404)
