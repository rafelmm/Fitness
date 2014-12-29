import datetime
from django.utils import timezone

from django.test import TestCase
from fitapp.models import Usuario

# Create your tests here.
class UsuarioDataTests(TestCase):
    
    def test_fecha_nacimiento_futura(self):
        time = timezone.now() + datetime.timedelta(days=30)
        usuario = Usuario(fecha_nacimiento = time)
        self.assertGreater(timezone.now(), usuario.fecha_nacimiento, "La fecha de nacimiento no puede ser futura")
        