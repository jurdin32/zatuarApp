from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Slider(models.Model):
    orden=models.IntegerField()
    slider=models.FileField(upload_to='slider', blank=True, null=True ,help_text='1884x529')

    def __str__(self):
        return ' %s ' % (self.slider)

    def vista_previa(self):
        return mark_safe('<image width="300" height="100"  src="/media/%s">' % self.slider)


    class Meta:
        verbose_name_plural="1. Slider"


class Zatuar_marca(models.Model):
    logo = models.FileField(upload_to='empresa/logo/', blank=True, null=True)
    logo_blanco = models.FileField(upload_to='empresa/logo/', blank=True, null=True)
    logo_negro = models.FileField(upload_to='empresa/logo/', blank=True, null=True)
    favicon = models.FileField(upload_to='empresa/logo/', blank=True, null=True)
    imagen = models.FileField(upload_to='empresa/logo/', blank=True, null=True, help_text='400x400')
    portada = models.FileField(upload_to='empresa/logo/', blank=True, null=True, help_text='1280x400')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.portada

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.logo)

    class Meta:
        verbose_name_plural = "2. Zatuar Marca"



class Contacto_empresa(models.Model):
    direccion=models.CharField(max_length=100,null=True,blank=True)
    calle=models.CharField(max_length=100,null=True,blank=True)
    mapa=models.TextField(max_length=500,null=True,blank=True)
    representante=models.CharField(max_length=100, null=True,blank=True)
    correo_personal=models.CharField(max_length=100, null=True,blank=True)
    celular=models.CharField(max_length=11,null=True,blank=True)
    celular2=models.CharField(max_length=100,null=True,blank=True)
    telefono=models.CharField(max_length=15,null=True,blank=True)
    correo=models.EmailField()
    horario=models.CharField(max_length=100, default=1, null=True, blank=True)
    horariosb=models.CharField(max_length=100, default=1, null=True, blank=True)

    class Meta:
        verbose_name_plural = "3. Contacto Empresa"


class Redes_sociales(models.Model):
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    behance = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "4. Redes Sociales"



class Beneficios(models.Model):
    beneficio=models.CharField( max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural="3. Zatuar Beneficios"


class Personalizaion_Poducto(models.Model):
    imagen=models.FileField(upload_to='producto')
    titulo=models.CharField(max_length=30,blank=True, null=True)
    descripcion=models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return ' %s ' % (self.imagen)

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.imagen)


    class Meta:
        verbose_name_plural="4. Perzonalizacion de Productos"



class Identidad(models.Model):
    titulo=models.CharField(max_length=30,blank=True, null=True)

    def __str__(self):
        return ' %s ' % (self.titulo)

    class Meta:
        verbose_name_plural="5. Zatuar es"

class Proceso(models.Model):
    detalle=models.CharField(max_length=200,blank=True, null=True)
    img1=models.FileField(upload_to='inicio',blank=True, null=True)
    ti1=models.CharField(max_length=30,blank=True, null=True)
    img2=models.FileField(upload_to='inicio', blank=True, null=True)
    ti2=models.CharField(max_length=30, blank=True, null=True)
    img3=models.FileField(upload_to='inicio', blank=True, null=True)
    ti3=models.CharField(max_length=30, blank=True, null=True)
    ti4 = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return ' %s ' % (self.detalle)

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.img1)


    class Meta:
        verbose_name_plural="6. Proceso"

class Galeria_Proceso(models.Model):
    imagen=models.FileField(upload_to='inicio',blank=True, null=True)
    titulo=models.CharField(max_length=30,blank=True, null=True)

    def __str__(self):
        return ' %s ' % (self.titulo)

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.imagen)


    class Meta:
        verbose_name_plural="7. Galeria_Proceso"



class Detalles(models.Model):
    titulo=models.CharField(max_length=30,blank=True, null=True)
    image1 = models.FileField(upload_to='detalles',blank=True, null=True)
    image2 = models.FileField(upload_to='detalles',blank=True, null=True)
    image3 = models.FileField(upload_to='detalles',blank=True, null=True)


    def __str__(self):
        return ' %s ' % (self.titulo)

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.image1)


    class Meta:
        verbose_name_plural="8. Detalles"


class Descarga(models.Model):
    orden = models.IntegerField()
    principal= models.BooleanField(default=False)
    img=models.FileField(upload_to='descarga',blank=True, null=True)
    titulo=models.CharField(max_length=30,blank=True, null=True)
    archivo=models.FileField(upload_to='descarga',blank=True, null=True)


    def __str__(self):
        return ' %s ' % (self.titulo)

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.img)


    class Meta:
        verbose_name_plural="9. Descarga"









class Casas(models.Model):
    color=models.CharField(max_length=40)
    duenio=models.CharField(max_length=40)
    valor=models.CharField(max_length=30,null=True,blank=True)
    fecha=models.DateTimeField(auto_now_add=True,null=True,blank=True)
