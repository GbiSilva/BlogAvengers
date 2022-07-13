from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from MarvelApp.models import Fases, Peliculas, Personajes, Personajes_Pelicula
from MarvelApp.forms import UserRegistrationForm, UserEditForm

# Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#@login_required
def inicio(request):
#    plantilla=loader.get_template('MarvelApp/inicio.html')
#    documento=plantilla.render()
#    return HttpResponse(documento)
    return render(request, 'MarvelApp/inicio.html', {'usuario': request.user.id})

def acerca(self):
    plantilla=loader.get_template('MarvelApp/acerca.html')
    documento=plantilla.render()
    return HttpResponse(documento)

#------------------------------------------------------------------------------------------------------------------
# FASES 
class FasesList(ListView):
  model = Fases
  template_name = 'MarvelApp/fases_list.html'

class FasesDetalle(DetailView):
  model = Fases
  template_name = 'MarvelApp/fases_detalle.html'

class FasesCreacion(CreateView):
  model = Fases
  fields = ['numero_romano']
  success_url = reverse_lazy('fases_listar') 

class FasesEdicion(UpdateView):
  model = Fases
  fields = ['numero_romano']
  success_url = reverse_lazy('fases_listar')

class FasesEliminacion(DeleteView):
  model = Fases
  success_url = reverse_lazy('fases_listar')

#------------------------------------------------------------------------------------------------------------------

# PELICULAS 
class PeliculasList(ListView):
  model = Peliculas
  template_name = 'MarvelApp/peliculas_list.html'

class PeliculasDetalle(DetailView):
  model = Peliculas
  template_name = 'MarvelApp/peliculas_detalle.html'

class PeliculasCreacion(CreateView):
  model = Peliculas
  fields = ['nombre', 'sinopsis', 'anio', 'duracion', 'nro_fase']
  success_url = reverse_lazy('peliculas_listar') 

class PeliculasEdicion(UpdateView):
  model = Peliculas
  fields = ['nombre', 'sinopsis', 'anio', 'duracion', 'nro_fase']
  success_url = reverse_lazy('peliculas_listar')

class PeliculasEliminacion(DeleteView):
  model = Peliculas
  success_url = reverse_lazy('peliculas_listar')

#------------------------------------------------------------------------------------------------------------------

# PERSONAJES 
class PersonajesList(ListView):
  model = Personajes
  template_name = 'MarvelApp/personajes_list.html'

class PersonajesDetalle(DetailView):
  model = Personajes
  template_name = 'MarvelApp/personajes_detalle.html'

class PersonajesCreacion(CreateView):
  model = Personajes
  fields = ['nombre', 'superpoder', 'actor_apellido', 'actor_nombre']
  success_url = reverse_lazy('personajes_listar') 

class PersonajesEdicion(UpdateView):
  model = Personajes
  fields = ['nombre', 'superpoder', 'actor_apellido', 'actor_nombre']
  success_url = reverse_lazy('personajes_listar')

class PersonajesEliminacion(DeleteView):
  model = Personajes
  success_url = reverse_lazy('personajes_listar')

#------------------------------------------------------------------------------------------------------------------

# PERSONAJES /PELICULAS
class Personajes_PeliculaList(ListView):
  model = Personajes_Pelicula
  template_name = 'MarvelApp/personajes_pelicula_list.html'

class Personajes_PeliculaDetalle(DetailView):
  model = Personajes_Pelicula
  template_name = 'MarvelApp/personajes_pelicula_detalle.html'

class Personajes_PeliculaCreacion(CreateView):
  model = Personajes_Pelicula
  fields = ['personaje', 'pelicula']
  success_url = reverse_lazy('personajes_pelicula_listar') 

class Personajes_PeliculaEdicion(UpdateView):
  model = Personajes_Pelicula
  fields = ['personaje', 'pelicula']
  success_url = reverse_lazy('personajes_pelicula_listar')

class Personajes_PeliculaEliminacion(DeleteView):
  model = Personajes_Pelicula
  success_url = reverse_lazy('personajes_pelicula_listar')

#------------------------------------------------------------------------------------------------------------------
# LOGIN

def login_request(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      usuario = form.cleaned_data.get('username')
      clave = form.cleaned_data.get('password')
      # Autenticación de usuario
      user = authenticate(username=usuario, password=clave) # Si este usuario existe me lo trae
      if user is not None:
        login(request,user) # Si existe, lo loguea
        return render(request, 'MarvelApp/inicio.html', {'mensaje': f'Bienvenido {usuario}'})
      else:
        return render(request, 'MarvelApp/inicio.html', {'mensaje': 'Error, datos incorrectos'})
    else:
      return render(request,'MarvelApp/inicio.html', {'mensaje': 'Error, formulario erróneo'})
  
  form = AuthenticationForm() # Creo un formulario vacío si vengo por GET
  return render(request, 'MarvelApp/login.html', {'form':form})

def registro(request):
  if request.method == 'POST': # Si es POST, entonces es un formulario que viene lleno
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      form.save()
      return render(request, 'MarvelApp/inicio.html', {'mensaje': f'Usuario {username} creado correctamente'})
    else:
      return render(request, 'MarvelApp/inicio.html', {'mensaje': 'Error, no se pudo crear el usuario'})
  else:
    form = UserRegistrationForm()
    return render(request, 'MarvelApp/registro.html', {'form': form})

@login_required
def editarPerfil(request):
  usuario = request.user

  if request.method == 'POST':
    formulario = UserEditForm(request.POST, instance=usuario)
    if formulario.is_valid():
      informacion = formulario.cleaned_data
      usuario.email = informacion['email']
      usuario.password1 = informacion['password1']
      usuario.password2 = informacion['password2']
      usuario.save()

      return render(request, 'MarvelApp/inicio.html', {'usuario': usuario, 'mensaje': 'Datos actualizados correctamente'})
  else:
    formulario = UserEditForm(instance=usuario)
  return render(request, 'MarvelApp/editarPerfil.html', {'formulario': formulario, 'usuario': usuario.username})