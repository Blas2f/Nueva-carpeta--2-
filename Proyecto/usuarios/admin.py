from django.contrib import admin
from .models import Categoria,Producto,pedido
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(pedido)