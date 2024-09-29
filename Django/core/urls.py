
from django.urls import path
from .views import index, cuenta, categoria, detailProduct, ingresar, recuperarClave,lista_clientes,listado_clientes_admin, editar_cliente
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView

urlpatterns = [
    path('',index, name="index"),    
    path('categoria/',categoria, name="categoria"),    
    path('cuenta/',cuenta, name="cuenta"),    
    path('detailProduct/',detailProduct, name="detailProduct"),    
    path('recuperarClave/',recuperarClave, name="recuperarClave"),    
    path('ingresar/',CustomLoginView.as_view(), name="ingresar"),  
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('clientes_admin/', listado_clientes_admin, name='listado_clientes_admin'),
    path('editar/<int:id>/', editar_cliente, name='editar_cliente'),
    
]   
