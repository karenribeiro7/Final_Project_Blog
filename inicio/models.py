from django.db import models

# Create your models here.

class Inicio(models.Model):
    titulo = models.CharField(max_length=100, default='')
    mensagem = models.TextField()
    autor = models.CharField(max_length=100, default='')
    imagem = models.ImageField(upload_to='inicio', null=True, blank=True)
    imagem_url = models.URLField(null=True, blank=True)
    data_postagem = models.DateTimeField(auto_now_add=True)