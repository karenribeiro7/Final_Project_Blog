from django.db import models
from django.contrib.auth.models import User

# class Inicio(models.Model):
#     titulo = models.CharField(max_length=100)
#     mensagem = models.TextField()
#     autor = models.ForeignKey(User, on_delete=models.CASCADE)
#     imagem = models.ImageField(upload_to='inicio', null=True, blank=True)
#     data_postagem = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.titulo
    
class Squad(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens/', blank=True)
    linkedin = models.CharField(max_length=250)
    github = models.CharField(max_length=250)

    def __str__(self):
        return self.nome

