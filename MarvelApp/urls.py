from django import views
from django.contrib import admin
from django.urls import path, include
from MarvelApp.views import inicio
from MarvelApp.views import fasesFormulario, peliculasFormulario, personajesFormulario, personajes_peliculaFormulario
from MarvelApp.views import busquedaPersonaje, resultadoPersonaje

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('fasesFormulario/', fasesFormulario, name="fasesFormulario"),
    path('peliculasFormulario/', peliculasFormulario, name="peliculasFormulario"),
    path('personajesFormulario/', personajesFormulario, name="personajesFormulario"),
    path('personajes_peliculaFormulario/', personajes_peliculaFormulario, name="personajes_peliculaFormulario"),
    path('busquedaPersonaje/', busquedaPersonaje, name="busquedaPersonaje"),
    path('resultadoPersonaje/', resultadoPersonaje, name="resultadoPersonaje"),
]
