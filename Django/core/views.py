from django.shortcuts import render
from .models import Categoria

# Create your views here.

def index(request):
    categoria = Categoria.objects.all()
    datos = {
        'categoria': categoria
    }
    return render(request, 'core/index.html',datos)

    