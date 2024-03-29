from django.urls import path
from categorias.views import categoria

app_name = 'categorias'
urlpatterns = [path('categoria/', categoria, name='categoria')]
