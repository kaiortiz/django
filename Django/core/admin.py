from django.contrib import admin
from .models import Categoria, Consola, Cliente

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Consola)
admin.site.register(Cliente)
