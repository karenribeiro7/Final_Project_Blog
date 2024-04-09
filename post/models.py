from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
# Create your models here.



class Post(models.Model):
    categoria = models.ForeignKey (Categoria, on_delete=models.CASCADE, null=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    titulo = models.CharField(max_length=150, null=False)
    slug = models.SlugField(unique=True, null=False)
    subtitulo = models.CharField(max_length=150, null=False)
    descricao = models.TextField(null=False)
    imagem = models.ImageField(upload_to='imagens/', null=True)
    texto = models.TextField(null=False)

    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_atualiacao = models.DateTimeField(auto_now=True)
