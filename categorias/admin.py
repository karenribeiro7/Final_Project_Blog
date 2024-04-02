from django.contrib import admin
from .models import Categoria

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug')
    list_filter = ('nome')
    search_fields = ('nome')
    prepopulated_fields = {'slug': ('nome',)}