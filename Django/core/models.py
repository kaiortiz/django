from django.db import models

# Create your models here.

#FALTA: ver bien lo de las FK, porque aún no estoy seguro cómo van.
#Los modelos están basados en la imagen que les envié por wsp.

#MODELO PARA CATEGORIA
class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True,verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')
    
    def __str__(self) :
        return self.nombreCategoria
    
#MODELO PARA CUENTAS DE USUARIO CLIENTE    
class Cuenta(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=30)
    nombreUsuario = models.CharField(max_length=20)
    correo = models.CharField(primary_key=True, max_length=30)
    clave = models.CharField(max_length=18)
    fechaNac = models.DateField()
    direccion = models.CharField(max_length=50)

    def __str__(self) :
        return self.correo

#MODELO PARA JUEGOS
class Juegos(models.Model):
    id_juego = models.CharField(max_length=10)
    nombreJuego = models.CharField(max_length=40)
    precio = models.IntegerField()
    stock = models.IntegerField()
    id_categoria = models.ForeignKey(Categoria)
    id_consola = models.ForeignKey(Consola)
    id_proveedor = models.ForeignKey(Proveedor)
    id_compra = models.ForeignKey(Compra)

    def __str__(self) :
        return self.nombreJuego
    
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

#MODELO COMPRA (BOLETA)
class Compra(models.Model):
    id_compra = models.CharField(primary_key=True, max_length=10)
    fecha_venta = models.DateField()
    hora_venta = models.TimeField()
    monto_venta = models.IntegerField()
    cantidad = models.IntegerField()
    Cuenta = models.ForeignKey(Cuenta)

    def __str__(self) :
        return self.id_compra

       
