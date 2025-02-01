'''from django.shortcuts import render

def home(request):
    return render(request, 'home.html')'''

from django.shortcuts import render
from produtos.models import Catalogo  

def home(request):
    catalogo_destaque = Catalogo.objects.filter(nome="Principais Ofertas!").first()
    return render(request, 'home.html', {'catalogo_destaque': catalogo_destaque})
