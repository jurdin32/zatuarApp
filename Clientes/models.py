from django.db import models

# Create your models here.
import uuid

from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils.safestring import mark_safe


class Cliente(models.Model):
    nombre_export = models.CharField(max_length=100, blank=True, null=True)
    client_logo = models.FileField(upload_to='cliente', blank=True, null=True, help_text='200x200')
    detalle = models.TextField(max_length=500, blank=True, null=True)
    foto = models.FileField(upload_to='cliente', blank=True, null=True, help_text='1280x500')
    pagweb = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(null=False, blank=True, unique=True)

    def __str__(self):
        return "%s" % self.nombre_export

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.client_logo)

    class Meta:
        verbose_name_plural = "8. Clientes"

def set_slug(sender, instance, *args, **kwargs): #callback
    if instance.nombre_export and not instance.slug:
        slug = slugify(instance.nombre_export)

        while Cliente.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.nombre_export, str(uuid.uuid4())[:8])
            )
        instance.slug = slug

pre_save.connect(set_slug, sender=Cliente)


class Galeria_Cliente(models.Model):
    cliente=models.ForeignKey(Cliente,  on_delete=models.CASCADE,null=True,blank=True)
    galeria=models.FileField(upload_to='cliente',blank=True, null=True, help_text='500x500')

    def vista_previa(self):
       if self.galeria:
            return """<a href="/media/%s"><img width="250" height="150" border="0" alt="Miniatura" src="/media/%s"/></a>""" % (self.galeria,self.galeria)
       else:
           return 'No hay imagen'

    vista_previa.short_description="vista_previa"
    vista_previa.allow_tags=True

    class Meta:
        verbose_name_plural="9.a Cliente Galeria"


class Producto_cliente(models.Model):
    client = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    imagen_producto = models.FileField(upload_to='producto', blank=True, null=True, help_text='500x500')
    portada = models.FileField(upload_to='producto', blank=True, null=True, help_text='600x400')

    def vista_producto(self):
        if self.imagen_producto:
            return """<a href="/media/%s"><img width="80" height="150" border="0" alt="Miniatura" src="/media/%s"/></a>""" % (
            self.imagen_producto, self.imagen_producto)
        else:
            return 'No hay imagen'

    vista_producto.short_description = "vista_producto"
    vista_producto.allow_tags = True

    class Meta:
        verbose_name_plural = "7. Mandil Cliente"

    def vista_portada(self):
        if self.portada:
            return """<a href="/media/%s"><img width="300" height="150" border="0" alt="Miniatura" src="/media/%s"/></a>""" % (
            self.portada, self.portada)
        else:
            return 'No hay imagen'

    vista_portada.short_description = "vista_portada"
    vista_portada.allow_tags = True
