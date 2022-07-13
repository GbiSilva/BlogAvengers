from django import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from MarvelApp.views import inicio, acerca, login_request, registro, editarPerfil
from MarvelApp.views import FasesList, FasesDetalle, FasesCreacion, FasesEdicion, FasesEliminacion
from MarvelApp.views import PeliculasList, PeliculasDetalle, PeliculasCreacion, PeliculasEdicion, PeliculasEliminacion
from MarvelApp.views import PersonajesList, PersonajesDetalle, PersonajesCreacion, PersonajesEdicion, PersonajesEliminacion
from MarvelApp.views import Personajes_PeliculaList, Personajes_PeliculaDetalle, Personajes_PeliculaCreacion, Personajes_PeliculaEdicion, Personajes_PeliculaEliminacion


urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('fases/', FasesList.as_view(), name='fases_listar'),
    path('fases/<pk>', FasesDetalle.as_view(), name='fases_detalle'),
    path('fases/nuevo/', FasesCreacion.as_view(), name='fases_crear'),
    path('fases/editar/<pk>', FasesEdicion.as_view(), name='fases_editar'),
    path('fases/borrar/<pk>', FasesEliminacion.as_view(), name='fases_borrar'),
    path('peliculas/', PeliculasList.as_view(), name='peliculas_listar'),
    path('peliculas/<pk>', PeliculasDetalle.as_view(), name='peliculas_detalle'),
    path('peliculas/nuevo/', PeliculasCreacion.as_view(), name='peliculas_crear'),
    path('peliculas/editar/<pk>', PeliculasEdicion.as_view(), name='peliculas_editar'),
    path('peliculas/borrar/<pk>', PeliculasEliminacion.as_view(), name='peliculas_borrar'),
    path('personajes/', PersonajesList.as_view(), name='personajes_listar'),
    path('personajes/<pk>', PersonajesDetalle.as_view(), name='personajes_detalle'),
    path('personajes/nuevo/', PersonajesCreacion.as_view(), name='personajes_crear'),
    path('personajes/editar/<pk>', PersonajesEdicion.as_view(), name='personajes_editar'),
    path('personajes/borrar/<pk>', PersonajesEliminacion.as_view(), name='personajes_borrar'),
    path('personajes_pelicula/', Personajes_PeliculaList.as_view(), name='personajes_pelicula_listar'),
    path('personajes_pelicula/<pk>', Personajes_PeliculaDetalle.as_view(), name='personajes_pelicula_detalle'),
    path('personajes_pelicula/nuevo/', Personajes_PeliculaCreacion.as_view(), name='personajes_pelicula_crear'),
    path('personajes_pelicula/editar/<pk>', Personajes_PeliculaEdicion.as_view(), name='personajes_pelicula_editar'),
    path('personajes_pelicula/borrar/<pk>', Personajes_PeliculaEliminacion.as_view(), name='personajes_pelicula_borrar'),
    path('acerca/', acerca, name="acerca"),
    path('login/', login_request, name = "Login"),
    path('registro', registro, name = "Registro"),
    path('logout', LogoutView.as_view(template_name='MarvelApp/logout.html'), name = "Logout"),
    path('editarPerfil', editarPerfil, name = "editarPerfil"),
]
