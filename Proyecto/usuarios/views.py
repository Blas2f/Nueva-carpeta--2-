from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def principal(request):
    context={}
    return render(request, 'principal.html', context)

def herramientas(request):
    context={}
    return render(request, 'herramientas.html', context)

def semillas(request):
    context={}
    return render(request, 'semillas.html', context)

def macetas(request):
    context={}
    return render(request, 'macetas.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Sesion iniciada correctamente"))
            return redirect('principal')
        else:
            messages.success(request, ("Error al iniciar sesion"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request,("Sesion cerrada correctamente"))
    return redirect('principal')

def registro(request):
    if  request.method == "POST":
        email   = request.POST['correo']
        username = request.POST['username']
        first_name = request.POST['p_nombre']
        last_name = request.POST['apellido']
        password = request.POST['password']

        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()

        return render(request,'registro.html', context)
    else:     
        user=User.objects.all()
        context={'user':user}
        return render(request,'registro.html', context)

def lista(request):
    user= User.objects.all()
    context={"user":user}
    return render(request, 'lista.html', context)

def borrar_user(request,pk):
    try:
        user=User.objects.get(username=pk)

        user.delete()
        user=User.objects.all()
        context = {'user':user}
        return render(request, 'lista.html', context)
    except:
        user=User.objects.all()
        context = {'user':user}
        return render(request, 'lista.html', context)

def modificar(request,pk):
    user=User.objects.get(username=pk)

    context={'user':user}
    if user:
        return render(request, 'lista.html', context)
    else:
        return render(request, 'lista.html', context)

def userUpdate(request):
    if request.method == "POST":
        email   = request.POST['correo']
        username = request.POST['username']
        first_name = request.POST['p_nombre']
        last_name = request.POST['apellido']
        password = request.POST['password']

        user=User()
        user.email=email
        user.username=username
        user.first_name=first_name
        user.last_name=last_name
        user.password=password
        user.save()
        context = {'user':user}
        return render(request, "editar.html", context)
    else:
        user = User.objects.all()
        context={'user':user}
        return render(request, "lista.html", context)






 