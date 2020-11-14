from django.urls import path

from .views import *

urlpatterns = [
    path('', ColorPaletteListView.as_view(), name='yourpalette'),
    path('<int:curso_id>/nuevo/', ColorPaletteCreateView.as_view(), name='yourpalette-new'),
    path('nuevo/', ColorPaletteCreateView.as_view(), name='yourpalette-new'),
    path('editar/<int:pk>', ColorPaletteUpdateView.as_view(), name='yourpalette-edit'),
    path('eliminar/<int:pk>', ColorPaletteDeleteView.as_view(), name='yourpalette-delete'),
    path('<int:pk>/', ColorPaletteDetailView.as_view(), name='yourpalette-detail'),
]
