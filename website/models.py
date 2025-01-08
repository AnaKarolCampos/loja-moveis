from django.db import models

class Catalogo(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to='produtos/')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Sobre(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='sobre/')

    def __str__(self):
        return self.titulo

class Contato(models.Model):
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.CharField(max_length=255)
    horario_funcionamento = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)

    def __str__(self):
        return "Contato"