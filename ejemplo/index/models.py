from django.db import models
from django.urls import reverse

# Create your models here.
        
class funado(models.Model):
    rut=models.CharField(primary_key=True, max_length=9)
    nombrefunado=models.CharField(max_length=200, help_text="Ingrese nombre del funado")
    des=models.TextField(max_length=1000, help_text="Descripcion de la funa")
    fecha=models.DateField()
    def __str__(self):
        return self.nombrefunado 