from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

# Construcción de Rest
from rest_framework.response import Response
#Construcción función a vista
from rest_framework.decorators import api_view
# Seguridad eliminada
from django.views.decorators.csrf import csrf_exempt
# Importación formato Json
from rest_framework.parsers import JSONParser
# Importación de código status
from rest_framework import status
# Importación de librería que  muestra mensaje not found 404
from django.shortcuts import get_list_or_404

from core.models import Proveedor
from .serializers import ProveedorSerializer, ProveedorPostSerializer
from core.models import Cuenta
from .serializers import CuentaSerializer, CuentaPostSerializer


@crsf_exempt
@api_view(['GET', 'POST'])
@permisson_classes((IsAuthenticated,))
def lista_proveedor(request):
    if request.method == 'GET':
        proveedor = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedor, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProveedorPostSerializer()

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


@crsf_exempt
@api_view(['GET', 'POST'])
@permisson_classes((IsAuthenticated,))
def lista_cuenta(request):
    if request.method == 'GET':
        proveedor = Cuenta.objects.all()
        serializer = CuentaSerializer(proveedor, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CuentaPostSerializer()

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)