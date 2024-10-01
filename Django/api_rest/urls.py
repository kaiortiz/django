from django.urls import path
from . import views

urlpatterns = [
    path('compra/', views.lista_Compras,name="lista_compras"),
    path('juegos/', views.lista_Juegos,name="lista_juegoss"),
    #path('compra/<id_compra>/', views.vista_cliente,name="vista_cliente"),
    
]