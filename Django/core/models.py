from django.db import models

# Create your models here.

#SuméAgragados el archivo e imagen del modelo relacioal en la carpeta del proyecto !

#MODELO PARA CATEGORIA
class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')
    
    def __str__(self) :
        return self.nombreCategoria
    
#MODELO PROVEEDOR DE JUEGOS
class Proveedor(models.Model):
    id_proveedor = models.CharField(primary_key=True, max_length=10)
    nombreProveedor = models.CharField(max_length=30)
    direccionProveedor = models.CharField(max_length=50)
    correoProvedor = models.CharField(max_length=40)
    numeroProveedor = models.IntegerField()

    def __str__(self) :
        return self.nombreProveedor

#MODELO CONSOLA
class Consola(models.Model):
    id_consola = models.CharField(primary_key=True, max_length=10)
    nombreConsola = models.CharField(max_length=20)

    def __str__(self) :
        return self.nombreConsola

#MODELO PARA JUEGOS
class Juegos(models.Model):
    id_juego = models.CharField(max_length=10)
    nombreJuego = models.CharField(max_length=40)
    precio = models.IntegerField()
    stock = models.IntegerField()
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_consola = models.ForeignKey(Consola, on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.nombreJuego
    
#MODELO COMPRA (BOLETA)
class Compra(models.Model):
    id_compra = models.CharField(primary_key=True, max_length=10)
    fecha_venta = models.DateField()
    hora_venta = models.TimeField()
    monto_venta = models.IntegerField()
    cantidad = models.IntegerField()
    id_juego = models.ForeignKey(Juegos,on_delete=models.CASCADE)

    def __str__(self) :
        return self.id_compra
    
#MODELO PARA CUENTAS DE USUARIO CLIENTE    
class Cuenta(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=30)
    nameUser = models.CharField(max_length=20)
    correo = models.CharField(primary_key=True, max_length=30)
    clave = models.CharField(max_length=18)
    fecNacimiento = models.DateField()
    direccion = models.CharField(max_length=50)
    #id_compra = models.ForeignKey(Compra,on_delete=models.CASCADE)

    def __str__(self) :
        return self.correo