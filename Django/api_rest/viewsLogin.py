from django.contrib.auth import authenticate 
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import get_list_or_404

@api_view(['POST0'])
def loginApi(request):
    data = JSONParser().parse(request)
    username = data.get('username')
    password = data.get('password')
                        
    if username is None or password is None:
        return Response('Se requiere el nombre o contraseña', status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username = username, password = password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response('Credenciales inválidas', status=status.HTTP_400_BAD_REQUEST)