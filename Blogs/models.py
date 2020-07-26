from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

itemCategoria=['categoria']
class Categoria(models.Model):
    categoria=models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):

        return '%s'%self.categoria

    class Meta:
        verbose_name_plural = "1. Categorias"

itemBlogs=['vista_previa','categoria','imagen','fecha','titulo','autor']
class Blogs(models.Model):
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagen=models.FileField(upload_to='blog/',help_text='imagen de 1280*500')
    fecha=models.DateField()
    titulo=models.TextField()
    articulo=models.TextField(max_length=10000, null=True, blank=True)
    autor=models.TextField()
    imagen2=models.FileField(upload_to='blog/', null=True,blank=True ,help_text='imagen de 1280*500')

    def __str__(self):

        return self.categoria.categoria

    def vista_previa(self):
        return mark_safe('<image width="300" height="150"  src="/media/%s">' % self.imagen)

    class Meta:
        verbose_name_plural = "2. Blogs"


itemVisitas_Blog=['blog','visita']
class Visitas_Blog(models.Model):
    blog=models.OneToOneField(Blogs, on_delete=models.CASCADE ,null=True,blank=True)
    visita=models.IntegerField(default=1)

    def visitar(self):
        return "<a target='blank' href='http://www.zatuar.com/blog/%s'>Ver en la Web</a>" % self.blog.id

    visitar.allow_tags = True
    visitar.short_description = "Ir"

    def save(self, *args, **kwargs):
        self.visita += 1
        super(Visitas_Blog, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "4. Visitas al Blog"


itemComentario=['blog','pregunta','usuario','fecha','email']
class Comentario (models.Model):
    blog=models.ForeignKey(Blogs,on_delete=models.CASCADE)
    pregunta=models.TextField()
    usuario=models.TextField()
    fecha=models.DateTimeField(auto_now_add=True)
    email=models.EmailField()

    def __str__(self):

        return self.pregunta

    class Meta:
        verbose_name_plural = "4. Comentarios"


itemRespuesta=['comentario','respuesta','usuario','fecha','email']
class Respuesta (models.Model):
    comentario=models.ForeignKey(Comentario,on_delete=models.CASCADE)
    respuesta=models.TextField()
    usuario=models.TextField()
    fecha=models.DateTimeField(auto_now_add=True)
    email=models.EmailField()

    class Meta:
        verbose_name_plural = "5. Respuestas"