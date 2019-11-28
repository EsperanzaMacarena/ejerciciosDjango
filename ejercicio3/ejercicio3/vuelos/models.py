from uuid import uuid4

from django.db import models
from django.db.models.deletion import SET_NULL


# Create your models here.
'''
Crear un nuevo proyecto Django, con una app llamada VUELOS, que sirva para manejar los 
diferentes vuelos que puede ofertar una determinada compañía aérea. Estas son las entidades que maneja:

Aeropuerto(nombre, ciudad, siglas)
Vuelo(aeropuerto_salida, fecha_salida, aeropuerto_llegada, fecha_llegada, codigo_vuelo)
Cliente(nombre,apellidos,email, fecha_nacimiento)
Reserva(vuelo, cliente, fecha_reserva, precio)

Algunas notas:
Un vuelo sale de un aeropuerto y llega a otro aeropuerto.
Las fechas de salida y llegada representan fecha y hora.
El código de vuelo no tiene que ser único a lo largo del tiempo

'''

class Aeropuerto(models.Model):
    id=models.UUIDField(primary_key=True,unique=True, default=uuid4,editable=False)
    nombre=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    siglas=models.CharField(max_length=3)
    
    def __str__(self):
        return self.nombre

class Vuelo(models.Model):
    id=models.UUIDField(primary_key=True, editable=False, default=uuid4)
    aeropuerto_salida=models.ForeignKey(Aeropuerto,related_name='aeropuerto_salida', on_delete=SET_NULL,null=True)
    aeropuerto_llegada=models.ForeignKey(Aeropuerto,related_name='aeropuerto_llegada',on_delete=SET_NULL,null=True)
    fecha_llegada=models.DateTimeField()
    fecha_salida=models.DateTimeField()
    codigo_vuelo=models.CharField(unique=False, max_length=10)

    def __str__(self):
        return self.fecha_salida+' salida desde '+self.aeropuerto_salida+' y llegada a '+self.aeropuerto_llegada +' '+self.fecha_llegada
    

class Cliente(models.Model):
    id=models.UUIDField(primary_key=True, editable=False, default=uuid4)
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()

    def __str__(self):
        return self.nombre+' '+self.apellidos

class Reserva(models.Model):
    vuelo= models.OneToOneField(Vuelo, on_delete=SET_NULL,null=True)
    cliente=models.OneToOneField(Cliente, on_delete=SET_NULL,null=True)
    fecha_reserva=models.DateField()
    precio=models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.cliente+' tiene reservado el vuelo '+self.vuelo+' para el día '+self.fecha_reserva+ ' a precio de '+self.precio+'€'