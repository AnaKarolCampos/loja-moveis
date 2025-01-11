from django.contrib import admin
from .models import Produto, Catalogo


admin.site.register(Produto)
admin.site.register(Catalogo)