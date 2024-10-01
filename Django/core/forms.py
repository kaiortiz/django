from django import forms
from .models import Cuenta

class RegistroClienteForms(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['nombre', 'apellidos','nameUser','correo', 'clave', 'fecNacimiento', 'direccion' ]
    
