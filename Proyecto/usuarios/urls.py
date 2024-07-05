from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.principal, name='principal'),
    path('herramientas/', views.herramientas, name='herramientas'),
    path('semillas/', views.semillas, name='semillas'),
    path('macetas/', views.macetas, name='macetas'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registro', views.registro, name='registro'),
    path('lista', views.lista, name='lista'),
    path('borrar_user/<str:pk>', views.borrar_user, name='borrar_user'),
    path('modificar/<str:pk>', views.modificar, name='modificar'),
    path('userUpdate', views.userUpdate, name='userUpdate'),



]    