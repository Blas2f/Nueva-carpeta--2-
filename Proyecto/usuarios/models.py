from django.db import models
import datetime
# Categorias de productos
class Categoria(models.Model):
    id_cat = models.CharField(max_length=3)
    nombre_cat = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_cat
    
# Detalle producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(default=0,decimal_places=2,max_digits=7)
    id_cat = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    id_prod = models.CharField(max_length=3, default=1)
    descripcion = models.CharField(max_length=250,default='', blank=True, null=True)

    en_venta = models.BooleanField(default=False)


    def __str__(self):
        return self.nombre


# 
class pedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    direccion = models.CharField(max_length=100, default='', blank=True)
    telefono = models.CharField(max_length=20, default='', blank=True)
    fecha = models.DateField(default=datetime.datetime.today)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.producto        
      
