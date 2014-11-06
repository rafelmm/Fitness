from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Dirección: contiene los campos necesarios para guardar la dirección postal
class Direccion(models.Model):
    calle = models.CharField(max_length=150, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    piso = models.CharField(max_length=5, blank=True, null=True)
    puerta = models.CharField(max_length=5, blank=True, null=True)
    escalera = models.CharField(max_length=5, blank=True, null=True)
    localidad = models.CharField(max_length=20, blank=True, null=True)
    cp = models.CharField(max_length=5,blank=True, null=True)

    def __str__(self):
        camposExtra = ''
        if (self.escalera is not None):
            camposExtra = ' esc. %s' % self.escalera
        if (self.piso is not None):
            camposExtra = '%s %s' % (camposExtra, self.piso,)
        if (self.puerta is not None):
            camposExtra = '%s%s' % (camposExtra, self.puerta,)
        return '%s %s%s,%s %s' %(self.calle, self.numero, camposExtra, self.cp, self.localidad,)

# Usuario: Pueden ser de distintos tipos segun al grupo al que pertenece
#   - Entrenador
#   - Socio
#   - Gestor
#   - Crear usuario:
#       >>> u = User.objects.create(username='...', password='...', ...)
#       >>> d = Direccion.objects.create(calle='...', numero='...', ...)
#       >>> usuario = Usuario.objects.create(user=u, direccion=d, ...)

class Usuario(models.Model):
    user = models.OneToOneField(User)
    direccion = models.ForeignKey(Direccion)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()
