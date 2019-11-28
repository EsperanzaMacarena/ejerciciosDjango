from django.contrib import admin

from productos.models import Categoria, Producto


# USUARIO SUPERADMIN = emescacena , 1
"""
Crear un nuevo proyecto Django, con una app llamada PRODUCTOS, que sirva para manejar un catálogo de productos representado por las siguientes entidades:

Producto(nombre, descripcion, url_imagen, precio_unidad, categoria)
Categoria(nombre, categoria_padre)

Algunas notas:
Un producto pertenece a una y solo una categoría
Una categoría no tiene porqué tener una categoría padre. 

"""
@admin.register(Producto)
class ProductosAdmin(admin.ModelAdmin):
    list_display=('nombre','descripcion','url_imagen','precio_unidad','categoria')
    list_filter=('categoria',)
    
@admin.register(Categoria) 
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nombre', 'categoria_padre')
