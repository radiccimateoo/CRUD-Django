from django.urls import path
from .views import personaView

urlpatterns = [
    path('registrarPersona/', personaView.registrar, name='registrar'),
    path('guardarPersona/', personaView.procesar),
    path('', personaView.listar, name='listaPersonas'),
    path('editarPersona/<int:id_persona>', personaView.editar, name='editar'),
    path('actualizarPersona/<int:id_persona>', personaView.actulizar),
    path('eliminarPersona/<int:id_persona>', personaView.eliminar, name='eliminar'),
]