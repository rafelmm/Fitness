from django.http import HttpResponse
from fitapp.models import Direccion

# Create your views here.
def index(request):
    return HttpResponse('Hello world, my name is Rafel and this is the first view')

def user_detail(request, user_id):
    
    return HttpResponse('This is the detail view for user %d' % int(user_id))

def address_list(request):
    address_list = Direccion.objects.all()
    output = ', '.join(a.__str__() for a in address_list)
    return HttpResponse(output)

