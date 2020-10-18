from django.shortcuts import render
from . models import elmanchas

# Create your views here.
def index(request):
    num=elmanchas.objects.all().count
    return render(request, 'index.html', context={'num':num}) 

def laheidi(request):
    return render(request, 'laheidi.html') 