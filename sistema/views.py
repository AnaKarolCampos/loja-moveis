from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def catalogo(request):
    return render(request, 'catalogo.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')