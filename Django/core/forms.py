from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Cliente

class RegistroClienteForms(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos','nameUser','correo', 'clave', 'fecNacimiento', 'direccion' ]
    
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nombre de usuario',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contraseña',
    }))
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos','nameUser','correo', 'clave', 'fecNacimiento', 'direccion' ]