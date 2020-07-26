from django.contrib import admin

# Register your models here.

from Clientes.models import *
from zatuarApp.snippers import Attr


class GaleriaInline(admin.StackedInline):
    model = Galeria_Cliente
    extra = 2

class ClienteAdmin(admin.ModelAdmin):
    list_display = Attr(Cliente)
    list_display_links = Attr(Cliente)
    inlines =[GaleriaInline]
admin.site.register(Cliente,ClienteAdmin)


class Galeria_ClienteAdmin(admin.ModelAdmin):
    list_display = Attr(Galeria_Cliente)
    list_display_links = Attr(Galeria_Cliente)
admin.site.register(Galeria_Cliente,Galeria_ClienteAdmin)




