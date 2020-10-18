from django.db import models
from django.urls import reverse

# Create your models here.
class elmanchas(models.Model):
    id=models.IntegerField(primary_key=True)  
    nombre=models.CharField(max_length=200, help_text="Ingrese nombre del manchas")
    def __str__(self):
        return str(self.id)
        
