from django.shortcuts import render
from .models import Categoria
from .forms import RegistroClienteForms
from django.contrib.auth.decorators import login_required

# request API
import requests

from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from django.shortcuts import render, redirect
from .models import Cliente

#Librerìas para editar y eliminar
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClienteForm
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

def login(request):
    return render (request, 'core/login.html')

def recuperarClave(request):
    return render (request, 'core/recuperarClave.html')





# DATA EDICION

class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
        super().__init__()
        
class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True


def index(request):
    if request.method == 'POST':
        form = RegistroClienteForms(request.POST)
        if form.is_valid():
            form.save()
            
            lista = ["Cuenta Corriente", "Deposito a Plazo", "Inversiones en BitCoin"]
            ##contexto = {"nombre":"Josè Acuña","productos":lista}
            cliente = Persona("José Acuña","34")
            contexto = {"cliente":cliente,"productos":lista}

            return render(request,'core/index.html',contexto)
    else:
        form = RegistroClienteForms()
    
    context = {
        'form': form,
        'cliente': request.user  # O el cliente que deseas mostrar, si es necesario
    }
    return render(request, 'core/index.html', context)

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/lista_clientes.html', {'clientes': clientes})

@login_required
def listado_clientes_admin(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/lista_clientes_admin.html', {'clientes': clientes})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm

# Vista para editar cliente
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('editar_cliente', id=cliente.id)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'core/editar_cliente.html', {'form': form, 'cliente': cliente})

# Vista para eliminar cliente
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listado_clientes_admin')
    return render(request, 'core/listado_clientes_admin.html', {'cliente': cliente})
