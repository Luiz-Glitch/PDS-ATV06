from django.contrib import admin
from .models import Escola
# Register your models here.

class EscolaAdmin(admin.ModelAdmin):
    list_display=['nome','local','nivel_de_ensino']

admin.site.register(Escola,EscolaAdmin)

