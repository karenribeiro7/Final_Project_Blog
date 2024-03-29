from django.db import models
from categorias.models import Categoria
# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=100, default='')
    mensagem = models.TextField()
    imagem = models.CharField(max_length=500, null=True, blank=True)
    # imagem = models.ImageField(upload_to='post', null=True, blank=True)
    # imagem_url = models.URLField(null=True, blank=True)
    categoria = models.ManyToManyField(Categoria)