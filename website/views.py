from django.shortcuts import render
from .models import Catalogo

def catalogo(request):
    produtos = Catalogo.objects.all()
    return render(request, 'catalogo.html', {'produtos': produtos})