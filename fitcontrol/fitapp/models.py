from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Direccion(models.Model):
    calle = models.CharField(max_length=150, blank=True)
    numero = models.CharField(max_length=20, blank=True)
    locality = models.CharField(max_length=20, blank=True)
    cp = models.PositiveIntegerField(null=False)

    def __str__(self):
        return '%s %s,%d %s' %(self.calle, self.numero, self.cp, self.locality,)
    
class Entrenador(models.Model):
    user = models.OneToOneField(User)
    direccion = models.ForeignKey(Direccion)
    telefono = models.CharField(max_length=15, blank=True)
    
class Socio(models.Model):
    user = models.OneToOneField(User)
    direccion = models.ForeignKey(Direccion)
    telefono = models.CharField(max_length=15, blank=True)
    
class Gestor(models.Model):
    user = models.OneToOneField(User)
    direccion = models.ForeignKey(Direccion)
    telefono = models.CharField(max_length=15, blank=True)
