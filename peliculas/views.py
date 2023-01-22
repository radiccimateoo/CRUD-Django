from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template.loader import get_template
from django.contrib.staticfiles import finders
from django.conf import settings

from .forms import formularioPersona, formularioPelicula, formularioPremio, formularioCine
from .models import tablaPersona, tablaPelicula, tablaPremio, tablaImagenes, tablaCines

from .insertar import *
from .convertir import *

import datetime
import os
# import base64

from xhtml2pdf import pisa


# Create your views here.
class personaView(HttpRequest):

    def registrarPersona(request):
        persona = formularioPersona()
        
        return render(request, 'registrarPersona.html', {'form': persona})

    def procesarPersona(request):
        persona = formularioPersona(request.POST)
        
        if persona.is_valid():
            persona.save()
            
            #insertar registros en el archivo.txt
            insertar(persona.save())
            persona = formularioPersona()
        
        return render(request, 'registrarPersona.html', {'form':persona, 'mensaje':'ok'})

    def editarPersona(request, id_persona):
        persona = tablaPersona.objects.filter(id= id_persona).first()
        form = formularioPersona(instance= persona)

        
        return render(request, 'editarPersona.html', {'form':form, 'persona':persona})

    def listarPersona(request):
        persona = tablaPersona.objects.all()
        
        return render(request, 'listaPersonas.html', {'personas':persona})

    def actulizarPersona(request, id_persona):
        persona =tablaPersona.objects.get(pk=id_persona)
        form = formularioPersona(request.POST, instance= persona)
        
        if form.is_valid():
            form.save()
        
        personas = tablaPersona.objects.all()

        return render(request, 'listaPersonas.html', {'personas': personas})

    def eliminarPersona(request, id_persona):
        persona = tablaPersona.objects.get(pk=id_persona)
        persona.delete()
        personas = tablaPersona.objects.all()

        return render(request, 'listaPersonas.html', {'personas': personas, 'mensaje':'ok'})
    

    def funciones_sueldos(request):
        datos = tablaPersona.objects.all()
        suma = 0
        cantidad_sueldos = 0
        persona_sueldo_bajo = ''
        sueldo_alto = datos[0].sueldo_mensual
        sueldo_bajo = datos[0].sueldo_mensual

        # calcular el promedio de los sueldos
        for sueldo in datos:
            suma += sueldo.sueldo_mensual
            cantidad_sueldos += 1
            

        sueldo_promedio = suma / cantidad_sueldos

        # calcular sueldo mas alto y obtener datos
        for dato in datos:
            if dato.sueldo_mensual > sueldo_alto:
                sueldo_alto = dato.sueldo_mensual
                persona_sueldo_alto = dato.nombre.capitalize(), dato.apellido.capitalize(), dato.dni
        
        # calcular sueldo mas bajo y obtener datos
        for dato in datos:
            if dato.sueldo_mensual < sueldo_bajo:
                sueldo_bajo = dato.sueldo_mensual
                persona_sueldo_bajo = dato.nombre.capitalize(), dato.apellido.capitalize(), dato.dni
        
        diferencia = sueldo_alto - sueldo_bajo
                

        return render(request, 'sueldos.html', 
            { 'sueldo_promedio': round(sueldo_promedio, 2),
              'sueldo_alto': sueldo_alto,
              'sueldo_bajo': sueldo_bajo,
              'datos_alto':persona_sueldo_alto,
              'datos_bajo':persona_sueldo_bajo,
              'diferencia': diferencia,
            }
        )

    def filtrar(request):
        encontrados = ''

        if 'nombre' in request.GET and 'dni' in request.GET:
            nombre = request.GET['nombre']
            dni = request.GET['dni']

        else:
            nombre = ''
            dni = 0
        
        encontrados = tablaPersona.objects.filter(nombre = nombre, dni = dni)
    
        return render(request, 'buscar.html', {'encontrados':encontrados, 'nombre':nombre, 'dni':dni})
    

    
    def sueldo_anual(request, sueldo):
        anual = sueldo * 12
    
        return render(request, 'anual.html', {'anual':anual})
    
    def edadActual(request, anio_nacimiento):
        fecha_atual = datetime.datetime.now()
        edad_actual = fecha_atual.year - anio_nacimiento

        return render(request, 'edadActual.html', {'actual': edad_actual})
    

    def actualizarSueldo(request, persona, sueldo, porcentaje):
        if porcentaje == 10:
            calculo = sueldo * 0.10
            final = sueldo + calculo
            person = tablaPersona.objects.filter(id=persona).update(sueldo_mensual = final)

        elif porcentaje == 15:
            calculo = sueldo * 0.15
            final = sueldo + calculo
            person = tablaPersona.objects.filter(id=persona).update(sueldo_mensual = final)

        else:
            if porcentaje == 20:
                calculo = sueldo * 0.20
                final = sueldo + calculo
                person = tablaPersona.objects.filter(id=persona).update(sueldo_mensual = final)
        
        personas = tablaPersona.objects.all()

        return render(request, 'listaPersonas.html', {'personas':personas})

    def consulta_join(request):
        pre = []
        pel = []

        premios = tablaPremio.objects.select_related('pelicula').all()
        peliculas = tablaPelicula.objects.select_related('persona').all()

        for premio in premios:
            p = premio.cantidad_nominaciones, premio.pelicula.nombre_pelicula
            pre.append(p)

        for pelicula in peliculas:
            p = pelicula.nombre_pelicula, pelicula.persona.nombre
            pel.append(p)

        return render(request, 'join.html', {'premios':pre, 'peliculas':pel})
    
    def leerInsert(request):
        archivo = leer()
        
        return render(request, 'leer.html', {'archivo':archivo})

    #TERMINAR Y POREGUNTAR
    def rango_sueldo(request):
        data = []
        tabla = tablaPersona.objects.all()

        return render(request, 'graficoSueldo.html', {'data': data})


class peliculaView(HttpRequest):

    def registrarPelicula(request):
        pelicula = formularioPelicula()
        
        return render(request, 'registrarPeliculas.html', {'formPelicula': pelicula})

    def procesarPelicula(request):
        pelicula = formularioPelicula(request.POST)
        
        if pelicula.is_valid():
            pelicula.save()
            insertar(pelicula.save())
            pelicula = formularioPelicula()
        
        return render(request, 'registrarPeliculas.html', {'formPelicula':pelicula, 'mensaje':'ok'})

    def editarPelicula(request, id_pelicula):
        pelicula = tablaPelicula.objects.filter(id= id_pelicula).first()
        formPelicula = formularioPelicula(instance= pelicula)
        
        return render(request, 'editarPelicula.html', {'formPelicula':formPelicula, 'pelicula':pelicula})

    def listarPelicula(request):
        pelicula = tablaPelicula.objects.all()

        return render(request, 'listaPeliculas.html', {'peliculas':pelicula})

    def actulizarPelicula(request, id_pelicula):
        pelicula =tablaPelicula.objects.get(pk=id_pelicula)
        formPelicula = formularioPelicula(request.POST, instance= pelicula)
        
        if formPelicula.is_valid():
            formPelicula.save()
        
        peliculas = tablaPelicula.objects.all()

        return render(request, 'listaPeliculas.html', {'peliculas': peliculas})

    def eliminarPelicula(request, id_pelicula):
        pelicula = tablaPelicula.objects.get(pk=id_pelicula)
        pelicula.delete()
        peliculas = tablaPelicula.objects.all()

        return render(request, 'listaPeliculas.html', {'peliculas': peliculas, 'mensaje':'ok'})
    
    def grafico_genero(request):
        generos = ['Accion','Aventura','Ciencia Ficcion','Comedia',
                    'No Ficcion','Drama','Fantasia','Musical','Suspenso','Terror']
        data = []
        
        for genero in generos:
            tabla = tablaPelicula.objects.filter(genero = genero.lower()).count()
            data.append(tabla)

        return render(request, 'graficoGenero.html', {'data':data})
        
class premioView(HttpRequest):
    def registrarPremio(request):
        premio = formularioPremio()
        
        return render(request, 'registrarPremios.html', {'formPremio': premio})

    def procesarPremio(request):
        premio = formularioPremio(request.POST)
        
        if premio.is_valid():
            premio.save()
            insertar(premio.save())
            premio = formularioPremio()
        
        return render(request, 'registrarPremios.html', {'formPremio':premio, 'mensaje':'ok'})

    def editarPremio(request, id_premio):
        premio = tablaPremio.objects.filter(id= id_premio).first()
        formpremio = formularioPremio(instance= premio)
        
        return render(request, 'editarPremio.html', {'formPremio':formpremio, 'premio':premio})

    def listarPremio(request):
        premio = tablaPremio.objects.all()

        return render(request, 'listaPremios.html', {'premios':premio})

    def actulizarPremio(request, id_premio):
        premio =tablaPremio.objects.get(pk=id_premio)
        formPremio = formularioPremio(request.POST, instance= premio)
        
        if formPremio.is_valid():
            formPremio.save()
        
        premios = tablaPremio.objects.all()

        return render(request, 'listaPremios.html', {'premios': premios})

    def eliminarPremio(request, id_premio):
        premio = tablaPremio.objects.get(pk=id_premio)
        premio.delete()
        premios = tablaPremio.objects.all()

        return render(request, 'listaPremios.html', {'premios': premios, 'mensaje':'ok'})

    
    def grafico_premio(request):
        conjunto_datos = []
        tabla = tablaPremio.objects.filter(cantidad_nominaciones__gte = 0)

        for i in tabla:
            datos = {
                'name': i.pelicula.nombre_pelicula, 
                'y': round(i.cantidad_nominaciones * 100 // 30, 2)
            }
            conjunto_datos.append(datos)

        return render(request, 'graficoPremio.html', {'data':conjunto_datos})


class imagenesView(HttpRequest):
    def imagenes(request):
        return render(request, 'imagenes.html')


class tablaImagenView(HttpRequest):

    def convertir(request):

        tablaFotos = tablaImagenes.objects.all()

        # ARREGLO PARA GUARDAR TODAS LAS IMAGENES DECODIFICADAS

        if 'imagen' in request.GET:
            imagen = request.GET['imagen']
            convertida = conversion(imagen)
        else:
            imagen = ''

        # GUARDANDO LAS FOTOS CONVERTIDAS EN LA TABLA
        tabla = tablaImagenes.objects.create(base=convertida)

        # DECODIFICANDO CADA UNA DE LAS FOTOS


        # return render(request, 'fotos.html', {'decodificado':decodificadas})

    def img(request):
        tablaFotos = tablaImagenes.objects.all()
        return render(request, 'fotos.html', {'tablaFotos':tablaFotos})


def media(uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path


def get(request):

        personas = tablaPersona.objects.all()

        plantilla = get_template('pdf.html')

        lista = []
        contador_sueldos = 0
        sumatoria_sueldos = 0

        for i in personas:
            sueldo = i.sueldo_mensual
            contador_sueldos += 1
            sumatoria_sueldos += sueldo 
            lista.append(sueldo)
        
        mayor = max(lista)
        menor = min(lista)
        promedio = sumatoria_sueldos / contador_sueldos
        diferencia = mayor - menor

        contexto = {
            'personas':personas,
            'logo': 'img/logo.png',
            'sueldo_promedio': round(promedio,2),
            'sueldo_alto':mayor,
            'sueldo_bajo':menor,
            'diferencia':diferencia,
        }

        html = plantilla.render(contexto) 
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="archivo.pdf"'
        pisaStatus = pisa.CreatePDF(html, dest=response, link_callback=media)

        if pisaStatus.err:
            return HttpResponse('hubo un error')

        return response


class CineView(HttpRequest):
    def registrarCine(request):
        cine = formularioCine()
        
        return render(request, 'registrarCine.html', {'formCine': cine})

    def procesarCine(request):
        cine = formularioCine(request.POST)
        
        if cine.is_valid():
            cine.save()
            insertar(cine.save())
            cine = formularioCine()
        
        return render(request, 'registrarCine.html', {'formCine':cine, 'mensaje':'ok'})

    def editarCine(request, id_cine):
        cine = tablaCines.objects.filter(id= id_cine).first()
        formcine = formularioCine(instance= cine)
        
        return render(request, 'editarCine.html', {'formCine':formcine, 'cine':cine})

    def listarCine(request):
        cine = tablaCines.objects.all()

        return render(request, 'listaCines.html', {'cines':cine})

    def actulizarCine(request, id_cine):
        cine =tablaCines.objects.get(pk=id_cine)
        formcine = formularioCine(request.POST, instance= cine)
        
        if formcine.is_valid():
            formcine.save()
        
        cines = tablaCines.objects.all()

        return render(request, 'listaCines.html', {'cines': cines})

    def eliminarCine(request, id_cine):
        cine = tablaCines.objects.get(pk=id_cine)
        cine.delete()
        cines = tablaCines.objects.all()

        return render(request, 'listaCines.html', {'cines': cines, 'mensaje':'ok'})
    
    def mapa(request):
        cines = tablaCines.objects.all()
        data = []
        for cine in cines:
            data.append(float(cine.latitud))
            data.append(float(cine.longitud))

        return render(request, 'mapa.html', {'data':data})