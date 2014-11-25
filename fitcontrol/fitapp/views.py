from django.shortcuts import render, get_object_or_404
from fitapp.models import Direccion, Usuario

# Create your views here.
def index(request):
    return render(request, 'fitapp/index.html', {})

def user_detail(request, user_id):
    
    usuario = get_object_or_404(Usuario, pk=user_id)
    context = {
        'usuario':  usuario,
    }
    return render(request, 'fitapp/user_detail.html', context)

def address_list(request):
    address_list = Direccion.objects.all()
    context = {'address_list': address_list}
    return render(request, 'fitapp/address_list.html', context)

