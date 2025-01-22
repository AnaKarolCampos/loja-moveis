from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
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
    
'''class Venda(models.Model):
    codigo = models.CharField(max_length=5)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateField()
    produtos = models.ManyToManyField(Produto)

    def __str__(self):
        return f"Venda {self.codigo} - {self.data_venda}"
'''
class Venda(models.Model):
    codigo = models.CharField(max_length=5)
    data_venda = models.DateField(auto_now_add=True)
    produtos = models.ManyToManyField(Produto)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calcular_total(self):
        return sum(produto.preco for produto in self.produtos.all())

    def save(self, *args, **kwargs):
        """ Salva a venda primeiro para gerar o ID, depois adiciona os produtos e recalcula o total """
        super().save(*args, **kwargs)  # Salva a venda para gerar o ID
        self.total = self.calcular_total()  # Agora que a venda tem ID, calcula o total
        super().save(*args, **kwargs)  # Salva novamente com o total atualizado

    def __str__(self):
        return f"Venda {self.codigo} - {self.data_venda} - Total: R${self.total}"

# Venda tem que ter o campo total, que tem que ser calculado na hora que a venda for salva
# categoria de produtos tem que ser uma lista para escolher
# cliente tem que ser linkado na venda, desce o model de cliente para a app produtos e linka no model de vendas com campo tipo ForeingKey