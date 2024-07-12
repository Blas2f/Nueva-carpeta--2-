from usuarios.models import Producto


class Cart():
    def __init__(self,request):
        self.session = request.session

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, producto):
        id_producto = str(producto.id_prod)

        if id_producto in self.cart:
            pass
        else:
            self.cart[id_producto] = {'precio prod': str(producto.precio)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)   

    def obt_prod(self):
        ids_productos = self.cart.keys()

        productos = Producto.objects.filter(id_prod__in=ids_productos)

        return productos
