from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from fitapp.models import Direccion, Usuario

def IndexView(request):
    return render(request, 'fitapp/index.html')

class UserDetailView(generic.DetailView):
    model = Usuario
    template_name = 'fitapp/user_detail.html'

class UserUpdateView(generic.DetailView):
    model = Usuario
    template_name = 'fitapp/user_update.html'
    
def user_update_action(request, usuario_id):
    u = get_object_or_404(Usuario, pk=usuario_id)
    try:
        nombre = request.POST['usuario-nombre']
        apellidos = request.POST['usuario-apellidos']
        dni = request.POST['usuario-dni']
        u.user.first_name = nombre
        u.user.last_name = apellidos
        u.dni = dni
        u.user.save()
        u.save()
    except:
        return render(request, 'fitapp/user_detail.html', {
            'error_message': "No se ha podido actualizar el usuario.",
        })
    else:
        return HttpResponseRedirect(reverse('fitapp:user_detail', args=(u.id,)))
    
def address_list(request):
    address_list = Direccion.objects.all()
    context = {'address_list': address_list}
    return render(request, 'fitapp/address_list.html', context)

