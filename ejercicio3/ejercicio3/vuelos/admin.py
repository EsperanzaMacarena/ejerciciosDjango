from django.contrib import admin

from vuelos.models import Aeropuerto, Cliente, Reserva, Vuelo


# Register your models here.
#superuser: emescacena , 1py
'''

Aeropuerto(nombre, ciudad, siglas)
Vuelo(aeropuerto_salida, fecha_salida, aeropuerto_llegada, fecha_llegada, codigo_vuelo)
Cliente(nombre,apellidos,email, fecha_nacimiento)
Reserva(vuelo, cliente, fecha_reserva, precio)

Algunas notas:
Un vuelo sale de un aeropuerto y llega a otro aeropuerto.
Las fechas de salida y llegada representan fecha y hora.
El código de vuelo no tiene que ser único a lo largo del tiempo

'''
@admin.register(Aeropuerto)
class AeropuertoAdmin(admin.ModelAdmin):
    list_display=('nombre','ciudad','siglas')

@admin.register(Vuelo)
class VueloAdmin(admin.ModelAdmin):
    list_display=('fecha_salida','aeropuerto_salida','fecha_llegada', 'aeropuerto_llegada','codigo_vuelo')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=('nombre','apellidos','email','fecha_nacimiento')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display=('vuelo','cliente','fecha_reserva','precio')


