from django.urls import path
from . import views

urlpatterns = [
    path('principal/', views.principal, name='principal'),
    path('herramientas/', views.herramientas, name='herramientas'),
    path('semillas/', views.semillas, name='semillas'),
    path('macetas/', views.macetas, name='macetas'),
    path('login/', views.login, name='login')

]    