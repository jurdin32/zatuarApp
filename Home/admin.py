from django.contrib import admin

# Register your models here.
from Home.models import *
from zatuarApp.snippers import Attr


class SliderAdmin(admin.ModelAdmin):
    list_display = Attr(Slider)
    list_display_links = Attr(Slider)



class Zatuar_marcaAdmin(admin.ModelAdmin):
    list_display = Attr(Zatuar_marca)
    list_display_links = Attr(Zatuar_marca)



class Contacto_empresaAdmin(admin.ModelAdmin):
    list_display = Attr(Contacto_empresa)
    list_display_links = Attr(Contacto_empresa)

class Redes_SocialesAdmin(admin.ModelAdmin):
    list_display = Attr(Redes_sociales)
    list_display_links = Attr(Redes_sociales)

class BeneficiosAdmin(admin.ModelAdmin):
    list_display = Attr(Beneficios)
    list_display_links = Attr(Beneficios)

class IdentidadAdmin(admin.ModelAdmin):
    list_display = Attr( Identidad)
    list_display_links = Attr( Identidad)

class Personalizacion_ProductoAdmin(admin.ModelAdmin):
    list_display = Attr(Personalizaion_Poducto)
    list_display_links = Attr(Personalizaion_Poducto)

class ProcesoAdmin(admin.ModelAdmin):
    list_display = Attr(Proceso)
    list_display_links = Attr(Proceso)


class Galeria_ProcesoAdmin(admin.ModelAdmin):
    list_display = Attr(Galeria_Proceso)
    list_display_links = Attr(Galeria_Proceso)
    list_filter = ['imagen', 'titulo']


class DescargaAdmin(admin.ModelAdmin):
    list_display = Attr(Descarga)
    list_display_links = Attr(Descarga)

class DetallesAdmin(admin.ModelAdmin):
    list_display = Attr(Detalles)
    list_display_links = Attr(Detalles)


class CasasAdmin(admin.ModelAdmin):
    list_display = Attr(Casas)
    list_display_links = Attr(Casas)

admin.site.register(Slider,SliderAdmin)
admin.site.register(Casas,CasasAdmin)
admin.site.register(Zatuar_marca, Zatuar_marcaAdmin)
admin.site.register(Contacto_empresa,Contacto_empresaAdmin)
admin.site.register(Redes_sociales,Redes_SocialesAdmin)
admin.site.register(Beneficios,BeneficiosAdmin)
admin.site.register(Personalizaion_Poducto,Personalizacion_ProductoAdmin)
admin.site.register(Identidad,IdentidadAdmin)
admin.site.register(Proceso,ProcesoAdmin)
admin.site.register(Galeria_Proceso,Galeria_ProcesoAdmin)
admin.site.register(Descarga,DescargaAdmin)
admin.site.register(Detalles,DetallesAdmin)
