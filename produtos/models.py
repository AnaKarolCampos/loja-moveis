from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=200)
    categoria = models.TextField(max_length=50)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    codigo = models.CharField(max_length=5)
    estoque = models.BooleanField(default=True) # colocar quantidade ao invés de 

    def __str__(self):
        return self.nome