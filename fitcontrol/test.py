from django.contrib.auth.models import User
from fitapp.models import Usuario
import datetime
def test():
    
    users = User.objects.all()
    if (len(users)>0):
        print(users)
        print('Borramos usuario')
        for u in users:
            u.delete()
        users = User.objects.all()
        print(users)
    
    usuario = Usuario(username='rafel', password='afaf', nombre='Rafel', apellidos='Mormeneo Melich', email='rafelmm@gmail.com', dni='47623078Z', fecha_nacimiento = datetime.datetime(1984,2,21))
    
    try:
        usuario.save()
    except Exception as e:
        print(e)
        
    print(User.objects.all())
    
    return usuario
 