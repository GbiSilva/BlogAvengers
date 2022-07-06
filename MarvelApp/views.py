from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from MarvelApp.models import Fases, Peliculas, Personajes, Personajes_Pelicula
from MarvelApp.forms import FasesFormulario, PeliculasFormulario
from MarvelApp.forms import PersonajesFormulario, Personajes_PeliculaFormulario

def inicio(self):
    plantilla=loader.get_template('MarvelApp/inicio.html')
    documento=plantilla.render()
    return HttpResponse(documento)

def fasesFormulario(request):
    if request.method == 'POST':
        mi_formulario = FasesFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nombre = informacion['nombre']
            grabar = Fases(nombre=nombre)
            grabar.save()
            return render(request, 'MarvelApp/inicio.html')
    else:
        mi_formulario = FasesFormulario()
    return render(request, 'MarvelApp/fasesFormulario.html', {'mi_formulario':mi_formulario})

def peliculasFormulario(request):
    if request.method == "POST":
        mi_formulario = PeliculasFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nombre = informacion['nombre']
            sinopsis = informacion['sinopsis']
            anio = informacion['anio']
            duracion = informacion['duracion']
            nombre_fase = informacion['nombre_fase']
            grabar = Peliculas(nombre=nombre, sinopsis=sinopsis, anio=anio, duracion=duracion, nombre_fase=nombre_fase)
            grabar.save()
            return render(request, 'MarvelApp/inicio.html')
    else:
        mi_formulario = PeliculasFormulario()
        return render(request, 'MarvelApp/peliculasFormulario.html', {'mi_formulario':mi_formulario})

def personajesFormulario(request):
    if request.method == "POST":
        mi_formulario = PersonajesFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nombre = informacion['nombre']
            superpoder = informacion['superpoder']
            actor_apellido = informacion['actor_apellido']
            actor_nombre = informacion['actor_nombre']
            grabar = Personajes(nombre=nombre,superpoder=superpoder, actor_apellido=actor_apellido, actor_nombre=actor_nombre)
            grabar.save()
            return render(request, 'MarvelApp/inicio.html')
    else:
        mi_formulario = PersonajesFormulario()
        return render(request, 'MarvelApp/personajesFormulario.html', {'mi_formulario':mi_formulario})

def personajes_peliculaFormulario(request):
    if request.method == "POST":
        mi_formulario = Personajes_PeliculaFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nombre_personaje = User.objects.get(nombre_personaje=request.POST['nombre_personaje'])
            nombre_pelicula = informacion['nombre_pelicula']
            grabar = Personajes_Pelicula(nombre_personaje=nombre_personaje, nombre_pelicula=nombre_pelicula)
            grabar.save()
            return render(request, 'MarvelApp/inicio.html')
    else:
        mi_formulario = Personajes_PeliculaFormulario()
        return render(request, 'MarvelApp/personajes_peliculaFormulario.html', {'mi_formulario':mi_formulario})

def busquedaPersonaje(request):
    return render(request, 'MarvelApp/busquedaPersonaje.html')

def resultadoPersonaje(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        personajes = Personajes.objects.filter(nombre=nombre)
        respuesta = render(request, 'MarvelApp/resultadobusquedaPersonaje.html', {'personajes':personajes,'nombre':nombre} )
        return HttpResponse(respuesta)
    else:
        respuesta = "No se ha ingresado el personaje a buscar"
        return HttpResponse(respuesta)

#class PeliculaCreateView(CreateView):
#    model = Peliculas
#    success_url: "/MavelApp/peliculas/list"
#    fields = ['nombre', 'sinopsis', 'anio', 'duracion', 'nombre_fase']