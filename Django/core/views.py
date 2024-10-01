from django.shortcuts import render
from .models import Categoria
from .forms import RegistroClienteForms


# request API
import requests

# Create your views here.

def index(request):
    #API BACK
    url = "https://rickandmortyapi.com/api/character"
    response  = requests.get(url)
    personajes = response.json().get('results',[])

    categoria = Categoria.objects.all()
    datos = {
        'categoria': categoria,
        'personajes' : personajes
    }
    return render(request, 'core/index.html',datos)


def categoria(request):
    categoria = Categoria.objects.all()
    datos = {
        'categoria': categoria
    }
    return render (request, 'core/categoria.html',datos)

def cuenta(request):
    
    if request.method == 'POST':
        form = RegistroClienteForms(request.POST)
        if form.is_valid():
            form.save()
            
        return render (request, 'core/cuenta.html')
    else:
        form = RegistroClienteForms()
        
    contexto = {
        'form': form,
        'cliente': request.user
    }
    return render (request, 'core/cuenta.html', contexto)
        

def detailProduct(request):
    return render (request, 'core/detailProduct.html')

def ingresar(request):
    return render (request, 'core/ingresar.html')

def recuperarClave(request):
    return render (request, 'core/recuperarClave.html')