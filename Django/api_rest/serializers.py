from rest_framework import serializers
from core.models import Proveedor
from core.models import Cuenta


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__' #traer todas las columnas

class ProveedorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'


class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__' #traer todas las columnas

class CuentaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'