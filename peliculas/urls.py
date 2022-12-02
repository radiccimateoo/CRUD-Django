from django.urls import path
from .views import personaView

urlpatterns = [
    path('registrarPersona/', personaView.index),
    path('guardarPersona/', personaView.procesar),
]