from django.db import models

# Create your models here.

#MODELO PARA CATEGORIA
class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True,verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')
    
    def __str__(self) :
        return self.nombreCategoria
    
class Cuenta(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=30)
    nombreUsuario = models.CharField()
    correo = models.CharField(primary_key=True)
    clave = models.CharField(max_length=18)
    fechaNac = models.DateField()
    direccion = models.CharField(max_length=50)

    def __str__(self) :
        return self.cuenta

       
