from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=200)
    categoria = models.TextField(max_length=50)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    codigo = models.CharField(max_length=5)
    estoque = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.nome
    
class Catalogo(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='catalogos/')
    ativo = models.BooleanField(default=True)
    produtos = models.ManyToManyField(Produto)

    def __str__(self):
        return self.nome
    
class Vendas(models.Model):
    codigo =  models.CharField(max_length=5)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateField()
    produtos = models.ManyToManyField(Produto)
    

    def str(self):
        return ''


# Venda tem que ter o campo total, que tem que ser calculado na hora que a venda for salva
# categoria de produtos tem que ser uma lista para escolher
# cliente tem que ser linkado na venda, desce o model de cliente para a app produtos e linka no model de vendas com campo tipo ForeingKey