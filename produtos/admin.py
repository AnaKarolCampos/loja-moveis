'''from django.contrib import admin
from .models import Produto, Catalogo, Venda


admin.site.register(Produto)
admin.site.register(Catalogo)
admin.site.register(Venda)
'''

from django.contrib import admin
from .models import Venda, Cliente, Produto, Catalogo

class VendaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'data', 'cliente', 'total')  
    list_filter = ('cliente',)  
    search_fields = ('codigo', 'cliente__nome')  
    ordering = ('-data',)  

    fieldsets = (
        (None, {
            'fields': ('codigo', 'cliente', 'produtos', 'total')
        }),
    )

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')  
    search_fields = ('nome', 'email')  

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'codigo')  
    list_filter = ('estoque',)  
    search_fields = ('nome', 'codigo')  

class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')  
    search_fields = ('nome',)  
    list_filter = ('ativo',)  
    filter_horizontal = ('produtos',)  # Melhor visualização para ManyToManyField

admin.site.register(Venda, VendaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Catalogo, CatalogoAdmin)