from django.contrib import admin
from .models import *

admin.site.register(Fases)
admin.site.register(Peliculas)
admin.site.register(Personajes)
admin.site.register(Personajes_Pelicula)

# usuario: marvel
# email: marvel@coder.com
# clave: universomarvel