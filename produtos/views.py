from django.shortcuts import render
from .models import Catalogo

'''def catalogo(request):
    catalogos = Catalogo.objects.filter(ativo=True)
    return render(request, 'catalogo.html', { 'catalogos': catalogos })'''

def catalogo(request):
    catalogo_destaque = Catalogo.objects.filter(nome="Principais Ofertas!", ativo=True).first()
    catalogos = Catalogo.objects.filter(ativo=True).exclude(id=catalogo_destaque.id) if catalogo_destaque else Catalogo.objects.filter(ativo=True)

    return render(request, 'catalogo.html', {'catalogos': catalogos})
