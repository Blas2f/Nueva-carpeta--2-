from django.contrib import admin
from .models import Categoria,Usuario,Producto,pedido
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(pedido)