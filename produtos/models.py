from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    codigo = models.CharField(max_length=5)
    estoque = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()

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
    
class Venda(models.Model):
    codigo = models.CharField(max_length=5)
    data = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, null=True)  # Referência ao cliente
    produtos = models.ManyToManyField('Produto')  # Relação muitos-para-muitos com Produto
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Campo para armazenar o total da venda

    def __str__(self):
        return f"Venda {self.codigo} - {self.data} - Total: R${self.total}"

# Sinal para atualizar o total da venda quando produtos forem adicionados/removidos
@receiver(m2m_changed, sender=Venda.produtos.through)
def atualizar_total_venda(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:  # Após adicionar/remover produtos
        instance.total = sum(produto.preco for produto in instance.produtos.all())
        instance.save()