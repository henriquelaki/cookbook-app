from django.contrib import admin
from .models import Pessoa
# Register your models here.


class ListaPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome', 'email')
    search_fields = ('nome', 'email')
    list_per_page = 30


admin.site.register(Pessoa, ListaPessoas)
