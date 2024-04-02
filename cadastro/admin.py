from django.contrib import admin
from cadastro.models import Cadastro
# Register your models here.



@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_cadastro')
    search_fields = ('nome', 'email')
    list_filter = ('data_cadastro')