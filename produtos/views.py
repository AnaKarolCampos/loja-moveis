from django.shortcuts import render
from .models import Catalogo

def catalogo(request):
    catalogos = Catalogo.objects.filter(ativo=True)

    return render(request, 'catalogo.html', { 'catalogos': catalogos })