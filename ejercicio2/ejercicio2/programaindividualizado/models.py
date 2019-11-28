from uuid import uuid4

from django.db import models
from django.db.models.deletion import SET_NULL

'''
Crear un nuevo proyecto Django, con una app llamada PROGRAMAINDIVIDUALIZADO, que nos permita gestionar los programas de atención individualizados de una residencia geriátrica. Estas son las entidades a manejar:

Residente(nombre, apellidos, fecha_nacimiento)
Familiar(nombre, apellidos, fecha_nacimiento, parentesco)
Informe(fecha_informe, Partes[1..*])
ParteInforme(tipo, valoracion_inicial, objetivos, informe) 

Algunas notas:
El tipo de ParteInforme puede tomar alguno de estos valores: SANTIARIA, FUNCIONAL, PSIQUICA, SOCIAL, TERAPIA OCUPACIONAL.
Las fechas no tienen porqué almacenar la hora.
Un informe consta de muchas partes.


'''
# Create your models here.

class Residente(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid4, editable=False)
    nombre=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField('Fecha de nacimiento')

class Familiar(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid4, editable=False)
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=100)
    fecha_nacimiento=models.DateField('Fecha de nacimiento')
    PARENTESCO=(
        ('H','Hijo'),
        ('S','Sobrino'),
        ('N','Nieto'),
        ('H','Hermano')
    )
    parentesco=models.CharField(max_length=1,choices=PARENTESCO,blank=False,null=False)

class Informe(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid4, editable=False)

    fecha_informe=models.DateField('Fecha de informe')

class ParteInforme(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid4, editable=False)

    TIPO=(
        ('S','Sanitaria'),
        ('F','Funcional'),
        ('P','Psiquica'),
        ('S','Social'),
        ('T','Terapia Ocupacional')
    )
    tipo=models.CharField(max_length=1,choices=TIPO,blank=False,null=False)
    valoracion_inicial=models.TextField(max_length=1200,blank=True)
    objetivos=models.TextField(max_length=200,blank=True)
    informe=models.ForeignKey(Informe, on_delete=SET_NULL,null=True)
