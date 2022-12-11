from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from .models import RecienNacido
from .models import Evolucion
# from .models import core

# Create your views here.
def inicio(request):
    return render(request,'core/inicio.html')

@login_required(login_url='user-login')
def evoluciones(request):
    user = request.user
    evolucion = Evolucion.objects.filter()
    reciennacido = RecienNacido.objects.filter()
    padres = RecienNacido.padres


    return render(request,'core/evoluciones.html', {'reciennacido': reciennacido, 'padres': padres, 'evolucion': evolucion})

@login_required(login_url='user-login')
@permission_required('core.view_reciennacido',login_url='user-login')
def reciennacidos(request):
    reciennacido = RecienNacido.objects.filter()
    padres = RecienNacido.padres


    return render(request,'core/reciennacidos.html', {'reciennacido': reciennacido, 'padres': padres})

def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return render(request, 'core/inicio.html')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'core/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'core/login.html')