from django.db import models

class Estoque(models.Model):
    produto = models.CharField(max_length=100)
    descricao = models.TextField(max_length=200)
    categoria = models.TextField(max_length=50)
    codigo = models.CharField(max_length=5)
    disponibilidade = models.BooleanField(default=True)

    def __str__(self):
        return self.produto
    
#sem model de estoque