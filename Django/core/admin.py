from django.contrib import admin
from .models import Categoria, Consola, Compra, Juegos, Proveedor, Cliente

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Consola)
admin.site.register(Compra)
admin.site.register(Juegos)
admin.site.register(Proveedor)
