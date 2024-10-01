from rest_framework import serializers
from core.models import Compra, Juegos

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__' #traer todos las columnas de la BD

class CompraPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ['id_compra','fecha_venta','hora_venta','monto_venta','cantidad','id_juego']
        
        
class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juegos
        fields = '__all__' #traer todos las columnas de la BD

class JuegoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juegos
        fields = ['id_juego','nombreJuego','precio','stock','id_categoria','id_consola','id_proveedor']
        
