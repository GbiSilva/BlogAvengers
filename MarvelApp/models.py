from django.db import models

class Fases(models.Model):
    numero_romano=models.CharField(max_length=3, help_text="Ingrese el nro de fase en numeros romanos")
    def __str__(self) -> str:
        return self.numero_romano

class Peliculas(models.Model):
    nombre=models.CharField(max_length=40, help_text="Ingrese el nombre de la película")
    sinopsis=models.TextField(help_text="Ingrese el resumen de la película")
    anio=models.IntegerField(help_text="Ingrese el año de estreno  de la película")
    duracion=models.IntegerField(help_text="Ingrese la duración en minutos de la película")
    nro_fase=models.ForeignKey(Fases, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nombre+" "+str(self.anio) 

class Personajes(models.Model):
    nombre=models.CharField(max_length=30, help_text="Ingrese el nombre del personaje")
    superpoder=models.CharField(max_length=30, help_text="Ingrese el superpoder del personaje")
    actor_apellido=models.CharField(max_length=30, help_text="Ingrese el apellido del actor")
    actor_nombre=models.CharField(max_length=30, help_text="Ingrese el nombre del actor")
    def __str__(self) -> str:
        return self.nombre
    
class Personajes_Pelicula(models.Model):
    personaje=models.ForeignKey(Personajes, on_delete=models.CASCADE)
    pelicula=models.ForeignKey(Peliculas, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.personaje)+"-"+str(self.pelicula)
