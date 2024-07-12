from django.shortcuts import render, get_object_or_404
from .cart import Cart
from django.http import JsonResponse
from usuarios.models import Producto
# Create your views here.
def cart_items(request):
    cart = Cart(request)
    productos_cart = cart.obt_prod
    return render(request, "cart_items.html", {"productos_cart":productos_cart})
 
def cart_agregar(request):

    cart = Cart(request)

    if request.POST.get('action') == 'post':

        id_producto = str(request.POST.get('id_prod'))

        producto = get_object_or_404(Producto, id_prod = id_producto)

        cart.add(producto=producto)


        response = JsonResponse({'Nombre:': producto.nombre})
        return response

def cart_eliminar(request):
    pass

def cart_modificar(request):
    pass