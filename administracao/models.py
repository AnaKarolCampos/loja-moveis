from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    categoria = models.CharField(max_length=100)

    def str(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()

    def str(self):
        return self.nome

class Vendas(models.Model):
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateField()
    

    def str(self):
        return self.descricao

# Create your models here.
