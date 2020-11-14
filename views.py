from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import ColorPalette
from .forms import ColorPaletteForm


class ColorPaletteListView(ListView):
    queryset = ColorPalette.objects.order_by('created_at')
    template_name = 'yourpalette/index.pug'
    model = ColorPalette

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ColorPaletteDetailView(DetailView):
    model = ColorPalette
    template_name = 'yourpalette/detail.pug'


class ColorPaletteCreateView(LoginRequiredMixin, CreateView):
    model = ColorPalette
    template_name = 'yourpalette/form.pug'
    form_class = ColorPaletteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'new'
        return context


class ColorPaletteUpdateView(LoginRequiredMixin, UpdateView):
    model = ColorPalette
    template_name = 'yourpalette/form.pug'
    form_class = ColorPaletteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'edit'
        return context


class ColorPaletteDeleteView(LoginRequiredMixin, DeleteView):
    model = ColorPalette
    success_url = reverse_lazy('yourpalette')

    def get(self, request, *args, **kwargs):
        try:
            object = ColorPalette.objects.get(pk=kwargs['pk'])
            return render(request, 'yourpalette/confirm_delete.html',
                          context={'object': object})
        except ColorPalette.DoesNotExist:
            return render(request, 'yourpalette/errors/404.html', status=404)
