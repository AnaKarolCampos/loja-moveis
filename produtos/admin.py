'''from django.contrib import admin
from .models import Produto, Catalogo, Venda


admin.site.register(Produto)
admin.site.register(Catalogo)
admin.site.register(Venda)
'''

from django.contrib import admin
from .models import Venda, Cliente, Produto

class VendaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'data', 'cliente', 'total')  # Exibir 'cliente' e 'total' na lista
    list_filter = ('cliente',)  # Filtrar vendas por cliente
    search_fields = ('codigo', 'cliente__nome')  # Permitir buscar vendas pelo nome do cliente
    ordering = ('-data',)  # Ordenar por data

    # Personalizar o formulário de venda no admin
    fieldsets = (
        (None, {
            'fields': ('codigo', 'cliente', 'produtos', 'total')
        }),
    )

admin.site.register(Venda, VendaAdmin)
admin.site.register(Cliente)
admin.site.register(Produto)
