from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'core/inicio.html')

def evoluciones(request):
    return render(request,'core/evoluciones.html')
