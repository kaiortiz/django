from django.urls import path
from .import views


urlpatterns = [
    path('Proveedor', views.lista_proveedor, name="lista_proveedor"),
]
