import uuid

from django.db import models

# Create your models here.
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils.safestring import mark_safe


class Ciudad(models.Model):
    ciudad = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return ' %s ' % (self.ciudad)

    class Meta:
        verbose_name_plural = "1. Ciudad"


class Proveedor(models.Model):
    proveedor = models.CharField(max_length=100, null=True, blank=True)
    logo = models.FileField(upload_to='proveedor/', null=True, blank=True)
    detalle = models.CharField(max_length=300, null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    correo = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return ' %s ' % (self.proveedor)

    class Meta:
        verbose_name_plural = "2. Proveedor"

class Clasif_producto(models.Model):
    clasificacion_producto = models.CharField(max_length=90, null=True, blank=True)

    def __str__(self):
        return ' %s ' % (self.clasificacion_producto)

    class Meta:
        verbose_name_plural = "3. Clasificaciòn de Producto"


class Product(models.Model):
    orden = models.IntegerField(default=0)
    clasif = models.ForeignKey(Clasif_producto, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    image_a = models.FileField(upload_to='products/', null=True, blank=True, help_text='100x100')
    image_b = models.FileField(upload_to='products/', null=True, blank=True, help_text='100x100')
    foto_slider = models.FileField(upload_to='producto/', null=True, blank=True)
    descripcion = models.TextField(max_length=500, null=True, blank=True)
    caracteristicas = models.TextField(max_length=500, null=True, blank=True)
    tamanos = models.CharField(max_length=500, null=True, blank=True)
    material = models.CharField(max_length=500, null=True, blank=True)
    textura = models.CharField(max_length=30, null=True, blank=True)
    gramaje = models.CharField(max_length=30, null=True, blank=True)
    nuevo = models.BooleanField(default=False)
    cantidad = models.IntegerField(null=True, blank=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    disponivilidad = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, blank=True, unique=True)

    def __str__(self):
        return ' %s ' % (self.title)

    def vista_previa(self):
        return mark_safe('<image width="100" height="100"  src="/media/%s">' % self.image_a)

    def vista_previa2(self):
        return mark_safe('<image width="100" height="100"  src="/media/%s">' % self.image_b)

    class Meta:
        verbose_name_plural = "4. Producto"


def set_slug(sender, instance, *args, **kwargs):  # callback
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:8])
            )
        instance.slug = slug


pre_save.connect(set_slug, sender=Product)



class Producto_Imagen(models.Model):
    orden = models.IntegerField(default=0)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    galeria_articulo = models.FileField(upload_to='media', help_text='imagen producto 800x800', null=True, blank=True)

    def __str__(self):
        return ' %s ' % (self.producto)

    def vista_previa(self):
        return mark_safe('<image width="50" height="70"  src="/media/%s">' % self.galeria_articulo)

    class Meta:
        verbose_name_plural = '5. Producto Imagenes'



class Producto_Personalizacion(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    imagen = models.FileField(upload_to='producto')
    titulo = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    def vista_previa(self):
        if self.imagen:
            return """<a href="/media/%s"><img width="60" height="60" border="0" alt="Miniatura" src="/media/%s"/></a>""" % (
            self.imagen, self.imagen)
        else:
            return 'No hay imagen'

    vista_previa.short_description = "vista_previa"
    vista_previa.allow_tags = True

    class Meta:
        verbose_name_plural = "6. Producto Personalizacion"



class Producto_Slider(models.Model):
    orden = models.IntegerField()
    producto = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    slider = models.FileField(upload_to='slider', blank=True, null=True, help_text='1884x529')

    def vista_previa(self):
        if self.slider:
            return """<a href="/media/%s"><img width="300" height="150" border="0" alt="Miniatura" src="/media/%s"/></a>""" % (
            self.slider, self.slider)
        else:
            return 'No hay imagen'

    vista_previa.short_description = "vista_previa"
    vista_previa.allow_tags = True

    class Meta:
        verbose_name_plural = "1. Slider"
