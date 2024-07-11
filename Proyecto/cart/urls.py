from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_items, name="cart_items"),
    path('agregar/', views.cart_agregar, name="cart_agregar"),
    path('eliminar/', views.cart_eliminar, name="cart_eliminar"),
    path('modificar/', views.cart_modificar, name="cart_modificar"),
]    