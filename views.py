from django.views.generic import ListView
from django.views.generic.base import ContextMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import FileResponse
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import ColorPalette
from .forms import ColorPaletteForm


class StylesheetHandlerView(DetailView):
    model = ColorPalette
    template_name = ''

    def get(self, request, *args, **kwargs):
        paleta = ColorPalette.objects.get(pk=kwargs['pk'])
        stylesheet = """
            .yp-bg-white {
              background-color: {{ white }};
            }
            .yp-fg-white {
              color: {{ white }};
            }
            .yp-bg-black {
              background-color: {{ black }};
            }
            .yp-fg-black {
              color: {{ black }};
            }
            .yp-bg-gray {
              background-color: {{ gray }};
            }
            .yp-fg-gray {
              color: {{ gray }};
            }
            .yp-bg-red {
              background-color: {{ red }};
            }
            .yp-fg-red {
              color: {{ red }};
            }
            .yp-bg-green {
              background-color: {{ green }};
            }
            .yp-fg-green {
              color: {{ green }};
            }
            .yp-bg-blue {
              background-color: {{ blue }};
            }
            .yp-fg-blue {
              color: {{ blue }};
            }
            .yp-bg-orange {
              background-color: {{ orange }};
            }
            .yp-fg-orange {
              color: {{ orange }};
            }
            .yp-bg-yellow {
              background-color: {{ yellow }};
            }
            .yp-fg-yellow {
              color: {{ yellow }};
            }
            .yp-bg-purple {
              background-color: {{ purple }};
            }
            .yp-fg-purple {
              color: {{ purple }};
            }
            .yp-bg-fuchsia {
              background-color: {{ fuchsia }};
            }
            .yp-fg-fuchsia {
              color: {{ fuchsia }};
            }
            .yp-bg-extra1 {
              background-color: {{ extra1 }};
            }
            .yp-fg-extra1 {
              color: {{ extra1 }};
            }
            .yp-bg-extra2 {
              background-color: {{ extra2 }};
            }
            .yp-fg-extra2 {
              color: {{ extra2 }};
            }
            .yp-bg-extra3 {
              background-color: {{ extra3 }};
            }
            .yp-fg-extra3 {
              color: {{ extra3 }};
            }
            .yp-bg-extra4 {
              background-color: {{ extra4 }};
            }
            .yp-fg-extra4 {
              color: {{ extra4 }};
            }
            .yp-bg-extra5 {
              background-color: {{ extra5 }};
            }
            .yp-fg-extra5 {
              color: {{ extra5 }};
            }

        """
        response = FileResponse(stylesheet)
        return response


class YourPaletteMixin(LoginRequiredMixin, PermissionRequiredMixin, ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(settings, 'YOURPALETTE_BASE_TEMPLATE'):
            context['base_template'] = settings.YOURPALETTE_BASE_TEMPLATE
        else:
            context['base_template'] = 'yourpalette/base/base.html'
        return context


class ColorPaletteListView(YourPaletteMixin, ListView):
    permission_required = 'yourpalette.can_view_colorpalette'
    queryset = ColorPalette.objects.order_by('created_at')
    template_name = 'yourpalette/list.html'
    model = ColorPalette


class ColorPaletteDetailView(YourPaletteMixin, DetailView):
    permission_required = 'yourpalette.can_view_colorpalette'
    model = ColorPalette
    template_name = 'yourpalette/detail.html'


class ColorPaletteCreateView(YourPaletteMixin, CreateView):
    permission_required = 'yourpalette.can_add_colorpalette'
    model = ColorPalette
    template_name = 'yourpalette/form.html'
    form_class = ColorPaletteForm

#    def get_form_kwargs(self):
#        kwargs = super().get_form_kwargs()
#        if kwargs['instance'] == None:
#            
#        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['action'] = 'new'
        return context


class ColorPaletteUpdateView(YourPaletteMixin, UpdateView):
    permission_required = 'yourpalette.can_change_colorpalette'
    model = ColorPalette
    template_name = 'yourpalette/form.html'
    form_class = ColorPaletteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'edit'
        return context


class ColorPaletteDeleteView(YourPaletteMixin, DeleteView):
    permission_required = 'yourpalette.can_delete_colorpalette'
    model = ColorPalette
    success_url = reverse_lazy('yourpalette')

    def get(self, request, *args, **kwargs):
        try:
            object = ColorPalette.objects.get(pk=kwargs['pk'])
            return render(request, 'yourpalette/confirm_delete.html',
                          context={'object': object})
        except ColorPalette.DoesNotExist:
            return render(request, 'yourpalette/errors/404.html', status=404)
