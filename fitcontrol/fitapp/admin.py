from django.contrib import admin
from django.contrib.auth.models import User
from fitapp.models import Usuario, Direccion

# Register your models here.

class DireccionInline(admin.StackedInline):
    model = Direccion
    extra = 1
    
class UsuarioInline(admin.StackedInline):
    model = Usuario
    
class UserAdmin(admin.ModelAdmin):
    #fields = ['username', 'first_name', 'last_name', 'email']
    inlines = [UsuarioInline, DireccionInline]

    list_display = ('username', 'email', 'first_name', 'last_name', 'es_mayor_edad', 'telefono', 'dni')
    search_fields = ['first_name', 'last_name', 'usuario__telefono', 'usuario__dni']
    
    def es_mayor_edad(self, obj):
        return obj.usuario.es_mayor_de_edad()
    es_mayor_edad.short_description = 'Mayor de edad'
    es_mayor_edad.boolean = True
    es_mayor_edad.admin_order_field = 'last_name'

    def telefono(self,obj):
        return obj.usuario.telefono
    telefono.short_description = 'Teléfono'
    telefono.admin_order_field = 'es_mayor_edad'

    def dni(self,obj):
        return obj.usuario.dni
    dni.short_description = 'DNI'
    dni.admin_order_field = 'telefono'
    
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
