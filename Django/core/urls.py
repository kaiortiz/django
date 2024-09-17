
from django.urls import path
from .views import index, cuenta, categoria, detailProduct, ingresar, recuperarClave

urlpatterns = [
    path('',index, name="index"),    
    path('categoria',categoria, name="categoria"),    
    path('cuenta',cuenta, name="cuenta"),    
    path('detailProduct',detailProduct, name="detailProduct"),    
    path('ingresar',ingresar, name="ingresar"),    
    path('recuperarClave',recuperarClave, name="recuperarClave"),    
    
]