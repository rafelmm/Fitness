# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from myException import MyException

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
    
    def __init__(self, username = None, password = None, email = None, nombre = None, apellidos = None, fecha_nacimiento = None, dni = None, telefono = None):
        models.Model.__init__(self)
        errorStr = ''
        error = False
        if (username is None or password is None):
            error = True
            errorStr = "El nombre de usuario y el password son obligatorios"
        
        self.user = User(username = username, password = password)
        self.user.email = email
        if (nombre is not None):
            self.user.first_name = nombre
        else:
            self.user.first_name = ''
            
        if (apellidos is not None):
            self.user.last_name = apellidos
        else:
            self.user.last_name = ''
        
        if (self.fecha_nacimiento > timezone.now()):
            error = True
            errorStr = "{0} {1}".format(errorStr, "La fecha de nacimiento no puede ser futura")
        
        self.fecha_nacimiento = fecha_nacimiento
        self.dni = dni
        self.telefono = telefono
        
        if (self.dni is not None and not self.validar_dni()):
            error = True
            errorStr = "{0} {1}".format(errorStr, "El DNI no tiene un formato valido")
        
        if (error is True):
            raise MyException(errorStr)
    
    def save(self, *args, **kwargs): 
        self.user.save()
        self.user_id = self.user.id
        try:
            models.Model.save(self, *args, **kwargs)
        except Exception as e:
            self.user.delete()
            raise MyException(e)
        
    def __str__(self):
        return self.user.get_full_name()

    def es_mayor_de_edad(self):
        return self.fecha_nacimiento.year+18 <= timezone.now().year

    def validar_dni(self):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dig_ext = "XYZ"
        reemp_dig_ext = {'X':'0', 'Y':'1', 'Z':'2'}
        numeros = "1234567890"
        dni = self.dni.upper()
        if len(dni) == 9:
            dig_control = dni[8]
            dni = dni[:8]
            if dni[0] in dig_ext:
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
            return len(dni) == len([n for n in dni if n in numeros]) \
                and tabla[int(dni)%23] == dig_control
        return False
    
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

