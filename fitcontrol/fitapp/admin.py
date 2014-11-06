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

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
