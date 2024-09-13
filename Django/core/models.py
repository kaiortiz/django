from django.db import models

# Create your models here.

#MODELO PARA CATEGORIA
class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True,verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')
    
    def __str__(self) :
        return self.nombreCategoria