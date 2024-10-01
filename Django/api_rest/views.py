from django.shortcuts import render
## Construcciòn de Rest
from rest_framework.response import Response
## Contrucciòn de de funciòn a vista
from rest_framework.decorators import api_view
## Seguridad eliminada
from django.views.decorators.csrf import csrf_exempt
##importaciòn formato Json
from rest_framework.parsers import JSONParser
##importaciòn de còdigo estatus
from rest_framework import status

from core.models import  Compra, Juegos
from .serializers import CompraSerializer,CompraPostSerializer, JuegoSerializer, JuegoPostSerializer

#Activar autenticaciòn
from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404



@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def lista_Compras(request):
    if request.method == 'GET':
        compra = Compra.objects.all()
        serializer = CompraSerializer(compra, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CompraPostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
        
def lista_Juegos(request):
    if request.method == 'GET':
        juego = Juegos.objects.all()
        serializer = JuegoSerializer(juego, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JuegoPostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
