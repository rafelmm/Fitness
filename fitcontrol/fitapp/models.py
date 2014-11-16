# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
    
# Usuario: Pueden ser de distintos tipos segun al grupo al que pertenece
#   - Entrenador
#   - Socio
#   - Gestor
class Usuario(models.Model):
    user = models.OneToOneField(User)
    dni = models.CharField(max_length=10, blank=False, null=False, default='00000000A')
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateTimeField('Fecha de nacimiento', default=timezone.now())
    
    def __str__(self):
        return self.user.get_full_name()

    def es_mayor_de_edad(self):
        return self.fecha_nacimiento.year+18 <= timezone.now().year

class IBAN(models.Model):
    user = models.OneToOneField(User)
    entidad = models.PositiveIntegerField(default=0,null=False)
    oficina = models.PositiveIntegerField(default=0,null=False)
    dc = models.PositiveIntegerField(default=0,null=False)
    cuenta = models.PositiveIntegerField(default=0,null=False)

    def __str__(self):
        return '%04d %04d %02d %10d' % (self.entidad, self.oficina, self.dc, self.cuenta)

    
# Dirección: contiene los campos necesarios para guardar la dirección postal
class Direccion(models.Model):
    user = models.ForeignKey(User, null=True)
    calle = models.CharField(max_length=150, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    piso = models.CharField(max_length=5, blank=True, null=True)
    puerta = models.CharField(max_length=5, blank=True, null=True)
    escalera = models.CharField(max_length=5, blank=True, null=True)
    localidad = models.CharField(max_length=20, blank=True, null=True)
    cp = models.CharField(max_length=5,blank=True, null=True)
    pais = models.CharField(max_length=2, null=False, default='ES')

    def __str__(self):
        camposExtra = ''
        if (self.escalera is not None and self.escalera != ''):
            camposExtra = ' esc. %s' % self.escalera
        if (self.piso is not None and self.piso != ''):
            camposExtra = '%s %s' % (camposExtra, self.piso,)
        if (self.puerta is not None and self.puerta != ''):
            camposExtra = '%s%s' % (camposExtra, self.puerta,)
        return '%s %s%s,%s %s' %(self.calle, self.numero, camposExtra, self.cp, self.localidad,)

