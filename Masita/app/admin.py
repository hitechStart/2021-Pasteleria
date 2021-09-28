from django.contrib import admin
from .models import Desayuno, Pasteleria

# Creamos una clase para poder modificar comportamiento del admin.
class ProyectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Registramos en admin el modelo y nuestro ProyectAdmin que tiene la cfg.
admin.site.register(Pasteleria, ProyectAdmin)
admin.site.register(Desayuno)


