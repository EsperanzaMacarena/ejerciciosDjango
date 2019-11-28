import uuid
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL


# Create your models here.
"""
Crear un nuevo proyecto Django, con una app llamada PRODUCTOS, que sirva para manejar un catálogo de productos representado por las siguientes entidades:

Producto(nombre, descripcion, url_imagen, precio_unidad, categoria)
Categoria(nombre, categoria_padre)

Algunas notas:
Un producto pertenece a una y solo una categoría
Una categoría no tiene porqué tener una categoría padre. 

"""

class Categoria(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    nombre=models.CharField(max_length=20)
    categoria_padre=models.ForeignKey('Categoria',on_delete=CASCADE,blank=True,null=True)
    
    class Meta:
        ordering=["nombre"]
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    nombre=models.CharField(max_length=20)
    descripcion=models.TextField('Descripcion',max_length=100)
    url_imagen=models.URLField('Imagen')
    precio_unidad=models.DecimalField('Precio',max_digits=6, decimal_places=2)
    categoria=models.ForeignKey(Categoria,on_delete=SET_NULL,null=True)

    class Meta:
        ordering=["nombre"]
        
    def __str__(self):
        return self.nombre+' | '+self.precio_unidad+'€ | '+self.categoria