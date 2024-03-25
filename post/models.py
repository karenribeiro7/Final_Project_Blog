from django.db import models
from django.utils import timezone


# Definindo o modelo para Post
class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now)
    categoria = models.ForeignKey('Categorias', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

# Definindo o modelo para Categorias
class Categorias(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome