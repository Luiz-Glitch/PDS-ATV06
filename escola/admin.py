from django.contrib import admin
from escola.models import Materia,Escola
# Register your models here.

class EscolaAdmin(admin.ModelAdmin):
    list_display=['nome','local','nivel_de_ensino']

admin.site.register(Escola,EscolaAdmin)

class MateriaAdmin(admin.ModelAdmin):
    list_display=['nome','hora_aula']

admin.site.register(Materia,MateriaAdmin)