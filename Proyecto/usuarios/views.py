from django.shortcuts import render

# Create your views here.
def principal(request):
    context={}
    return render(request, 'usuarios/principal.html', context)

def herramientas(request):
    context={}
    return render(request, 'usuarios/herramientas.html', context)

def semillas(request):
    context={}
    return render(request, 'usuarios/semillas.html', context)

def macetas(request):
    context={}
    return render(request, 'usuarios/macetas.html', context)

def login(request):
    context={}
    return render(request, 'usuarios/login.html', context)    

