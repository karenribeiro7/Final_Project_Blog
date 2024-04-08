from django.contrib import admin
from cadastro.models import Cadastro, Login
# Register your models here.

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data')
    search_fields = ('nome', 'email')
    list_filter = ('data', 'nome')

class LoginAdmin(admin.ModelAdmin):
    list_display = ('email', 'senha')
    search_fields = ('email', 'senha')
    list_filter = ('email', 'senha')

admin.site.register(Cadastro, Login)

