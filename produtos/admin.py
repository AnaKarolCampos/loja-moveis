from django.contrib import admin
from .models import Produto, Catalogo, Venda


admin.site.register(Produto)
admin.site.register(Catalogo)
admin.site.register(Venda)