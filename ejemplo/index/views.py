from django.shortcuts import render
from . models import funado

# Create your views here.
def index(request):
    return render(request, 'index.html') 

def laheidi(request):
    return render(request, 'laheidi.html') 

def funado(request):
    listafuna=funado.objects.all()
    return render(request, 'funados.html', context={'listafuna':listafuna})

