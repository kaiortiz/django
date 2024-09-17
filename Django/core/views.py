from django.shortcuts import render
from .models import Categoria

# Create your views here.

def index(request):
    categoria = Categoria.objects.all()
    datos = {
        'categoria': categoria
    }
    return render(request, 'core/index.html',datos)


def categoria(request):
    return render (request, 'core/categoria.html')

def cuenta(request):
    return render (request, 'core/cuenta.html')

def detailProduct(request):
    return render (request, 'core/detailProduct.html')

def ingresar(request):
    return render (request, 'core/ingresar.html')

def recuperarClave(request):
    return render (request, 'core/recuperarClave.html')