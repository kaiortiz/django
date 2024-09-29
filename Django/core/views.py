from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .models import Categoria
from .forms import  CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistroClienteForms
from .models import Cliente

#Librerìas para editar y eliminar
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClienteForm


# Create your views here.

def index(request):
    categoria = Categoria.objects.all()
    datos = {
        'categoria': categoria
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


class CustomLoginView(LoginView):
    template_name = 'core/ingresar.html'
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True
    
    
@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/lista_clientes.html', {'clientes': clientes})

@login_required
def listado_clientes_admin(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/lista_clientes_admin.html', {'clientes': clientes})

@login_required
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
