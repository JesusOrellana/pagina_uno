from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('laheidi',views.laheidi, name='laheidi'), 
    path('funado',views.funado, name='funado'),
]

