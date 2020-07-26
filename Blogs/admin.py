from django.contrib import admin

# Register your models here.
from Blogs.models import *
from zatuarApp.snippers import Attr


class CategoriaAdmin(admin.ModelAdmin):
    list_display = Attr(Categoria)
    list_display_links = Attr(Categoria)


class BlogsAdmin(admin.ModelAdmin):
    list_display = Attr(Blogs)
    list_display_links = Attr(Blogs)


#class BlogVisitaAdmin(admin.ModelAdmin):
    #list_display = itemVisitas_Blog
    #list_display_links = itemVisitas_Blog


class ComentarioAdmin(admin.ModelAdmin):
    list_display = Attr(Comentario)
    list_display_links = Attr(Comentario)


class RespuestaAdmin(admin.ModelAdmin):
    list_display = Attr(Respuesta)
    list_display_links = Attr(Respuesta)

admin.site.register(Blogs,BlogsAdmin)
#admin.site.register(Visitas_Blog,BlogVisitaAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Comentario,ComentarioAdmin)
admin.site.register(Respuesta)