from django.contrib import admin

# Register your models here.
from Productos.models import *
from zatuarApp.snippers import Attr


class CiudadAdmin(admin.ModelAdmin):
    list_display = Attr(Ciudad)
    list_display_links = Attr(Ciudad)

class ProveedorAdmin(admin.ModelAdmin):
    list_display = Attr(Proveedor)
    list_display_links = Attr(Proveedor)

class ProductAdminn(admin.ModelAdmin):
    list_display = Attr(Product)
    list_display_links = Attr(Product)

class Clasif_productoAdmin(admin.ModelAdmin):
    list_display = Attr(Clasif_producto)
    list_display_links = Attr(Clasif_producto)

class Producto_ImagenAdmin(admin.ModelAdmin):
    list_display = Attr(Producto_Imagen)
    list_display_links = Attr(Producto_Imagen)


class Producto_PersonalizacionAdmin(admin.ModelAdmin):
    list_display = Attr(Producto_Personalizacion)
    list_display_links = Attr(Producto_Personalizacion)


admin.site.register(Ciudad,CiudadAdmin)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Clasif_producto,Clasif_productoAdmin)
admin.site.register(Product,ProductAdminn)
admin.site.register(Producto_Imagen,Producto_ImagenAdmin)
admin.site.register(Producto_Personalizacion,Producto_PersonalizacionAdmin)