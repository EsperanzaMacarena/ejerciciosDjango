from django.contrib import admin

from programaindividualizado.models import (Familiar, Informe, ParteInforme,
                                            Residente)

# Register your models here.
#superuser : emescacena , 1

@admin.register(Familiar)
class FamiliarAdmin(admin.ModelAdmin):
    list_display=('nombre','apellidos','fecha_nacimiento','parentesco')
    list_filter=('parentesco',)

@admin.register(ParteInforme)
class ParteInformeAdmin(admin.ModelAdmin):
    list_display=('tipo','valoracion_inicial','objetivos','informe')
    list_filter=('tipo',)
    
@admin.register(Residente)
class ResidenteAdmin(admin.ModelAdmin):
    list_display=('nombre','fecha_nacimiento')

admin.site.register(Informe)
