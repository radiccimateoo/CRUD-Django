from django.urls import path
from .views import personaView

urlpatterns = [
    path('registrarPersona/', personaView.registrar, name='registrar'),
    path('guardarPersona/', personaView.procesar, name='guardar'),
    path('', personaView.listar, name='listaPersonas'),
    path('editarPersona/<int:id_persona>', personaView.editar, name='editar'),
    path('actualizarPersona/<int:id_persona>', personaView.actulizar, name='actualizar'),
    path('eliminarPersona/<int:id_persona>', personaView.eliminar, name='eliminar'),
]