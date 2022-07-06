from django import forms
from MarvelApp.models import Fases, Peliculas, Personajes

class FasesFormulario(forms.Form):
    nombre=forms.CharField(max_length=2)

from django import forms


class PeliculasFormulario(forms.Form):
    fases = Fases.objects.all()

    lista_fases = []
    for fase in fases:
        lista_fases = lista_fases + [('Fase ' + fase.nombre, fase.nombre)]
    
    nombre=forms.CharField(max_length=40)
    sinopsis=forms.CharField(widget=forms.Textarea)
    anio=forms.IntegerField()
    duracion=forms.IntegerField()
    nombre_fase=forms.ChoiceField(widget=forms.RadioSelect, choices=lista_fases)
    
class PersonajesFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    superpoder=forms.CharField(max_length=30)
    actor_apellido=forms.CharField(max_length=30)
    actor_nombre=forms.CharField(max_length=30)
    
class Personajes_PeliculaFormulario(forms.Form):
    peliculas = Peliculas.objects.all()
    lista_peliculas = []
    for pelicula in peliculas:
        lista_peliculas = lista_peliculas + [(pelicula.nombre, pelicula.nombre)]

    personajes = Personajes.objects.all()
    lista_personajes = []
    for personaje in personajes:
        lista_personajes = lista_personajes + [(personaje.nombre, personaje.nombre)]

    nombre_personaje=forms.ChoiceField(widget=forms.RadioSelect, choices=lista_personajes)
    nombre_pelicula=forms.ChoiceField(widget=forms.RadioSelect, choices=lista_peliculas)
