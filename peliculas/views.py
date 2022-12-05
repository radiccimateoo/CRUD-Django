from django.shortcuts import render
from django.http import HttpRequest

from .forms import formularioPersona
from .models import tablaPersona

# Create your views here.
class personaView(HttpRequest):

    def registrar(request):
        persona = formularioPersona()
        
        return render(request, 'registrarPersona.html', {'form': persona})

    def procesar(request):
        persona = formularioPersona(request.POST)
        
        if persona.is_valid():
            persona.save()
            persona = formularioPersona()
        
        return render(request, 'registrarPersona.html', {'form':persona, 'mensaje':'ok'})

    def editar(request, id_persona):
        persona = tablaPersona.objects.filter(id= id_persona).first()
        form = formularioPersona(instance= persona)
        
        return render(request, 'editarPersona.html', {'form':form, 'persona':persona})

    def listar(request):
        persona = tablaPersona.objects.all()

        return render(request, 'listaPersonas.html', {'personas':persona})

    def actulizar(request, id_persona):
        persona =tablaPersona.objects.get(pk=id_persona)
        form = formularioPersona(request.POST, instance= persona)
        
        if form.is_valid():
            form.save()
        
        personas = tablaPersona.objects.all()

        return render(request, 'listaPersonas.html', {'personas': personas})

    def eliminar(request, id_persona):
        persona = tablaPersona.objects.get(pk=id_persona)
        persona.delete()
        personas = tablaPersona.objects.all()

        return render(request, 'listaPersonas.html', {'personas': personas, 'mensaje':'ok'})
