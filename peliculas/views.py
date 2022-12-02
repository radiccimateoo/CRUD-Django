from django.shortcuts import render
from django.http import HttpRequest

from .forms import formularioPersona

# Create your views here.
class personaView(HttpRequest):

    def index(request):
        persona = formularioPersona()
        return render(request, 'documento.html', {'form': persona})

    def procesar(request):
        persona = formularioPersona(request.POST)
        if persona.is_valid():
            persona.save()
            persona = formularioPersona()
        
        return render(request, 'documento.html', {'form':persona, 'mensaje':'ok'})
