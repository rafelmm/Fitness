from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from fitapp.models import Direccion, Usuario

def IndexView(request):
    return render(request, 'fitapp/index.html')

class UserListView(generic.ListView):
    template_name = 'fitapp/user_list.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        """Return all the users."""
        return Usuario.objects.all()
    
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


class AddressUpdateView(generic.DetailView):
    model = Direccion
    template_name = 'fitapp/address_update.html'
    
def address_update_action(request, direccion_id):
    d = get_object_or_404(Direccion, pk=direccion_id)
    try:
        d.calle = request.POST['direccion-calle']
        d.numero = request.POST['direccion-numero']
        d.piso = request.POST['direccion-piso']
        d.puerta = request.POST['direccion-puerta']
        d.escalera = request.POST['direccion-escalera']
        d.localidad = request.POST['direccion-localidad']
        d.cp = request.POST['direccion-cp']
        d.pais = request.POST['direccion-pais']
        d.save()
    except:
        return render(request, 'fitapp/address_update.html', {
            'error_message': "No se ha podido actualizar la direccion.",
        })
    else:
        return HttpResponseRedirect(reverse('fitapp:user_detail', args=(d.user.id,)))