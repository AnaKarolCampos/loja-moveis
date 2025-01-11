from django.contrib import admin
from .models import Produto, Catalogo, Vendas


admin.site.register(Produto)
admin.site.register(Catalogo)
admin.site.register(Vendas)