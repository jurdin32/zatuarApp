from itertools import product

from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from Blogs.models import Categoria, Blogs, Visitas_Blog, Comentario, Respuesta
from Clientes.models import *
from Home.models import *
from django.shortcuts import *

from Productos.models import *


def blog_paginado(request):
    list = Blogs.objects.all().order_by("-fecha")
    paginator = Paginator(list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        blogss = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogss = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogss = paginator.page(paginator.num_pages)
    return blogss




def index(request):
    contexto = {
        "sliders": Slider.objects.all().order_by("orden"),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
        'personalizacion': Personalizaion_Poducto.objects.all(),
        'proceso': Proceso.objects.all().first(),
        'galeri_proces': Galeria_Proceso.objects.all(),
        'catalogo': Descarga.objects.all().first(),
        'identidad': Identidad.objects.all(),
        'detalles': Detalles.objects.first(),
        'clientes': Cliente.objects.all(),
    }
    return render(request,"index.html",contexto)

def empresa(request):
    contexto={
        'zatuar': Zatuar_marca.objects.all().first(),
        'beneficio':Beneficios.objects.all(),
        'proceso': Proceso.objects.all().first(),
        'contacto':Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
    }
    return render(request,"empresa.html",contexto)


def producto(request):
    contexto = {
        'clasif_producto': Clasif_producto.objects.all(),
        'product': Product.objects.all().order_by('-id'),
        'producto_personalizacion':Producto_Personalizacion.objects.all(),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
    }
    return render(request,"productos.html", contexto)


def producto_cate(request, id):
    contexto = {
        'clasif_producto': Clasif_producto.objects.all(),
        'product': Product.objects.filter(clasif_id=id),
        # 'producto_personalizacion': Producto_Personalizacion.objects.all(),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),

    }
    return render(request, 'productos.html', contexto,)


def producto_id(request, id):
    contexto = {
        'clasif_producto': Clasif_producto.objects.all(),
        'product': Product.objects.get(id=id),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),

    }
    return render(request, 'product.html', contexto,)

def clientes(request):
    contexto={
        'client':Cliente.objects.all(),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),

    }
    return render(request, 'clientes.html', contexto)

def clientes_id(request,id):
    client=Cliente.objects.get(id=id)
    galeria_cliente=Galeria_Cliente.objects.filter(cliente=client)
    zatuar=Zatuar_marca.objects.get()
    contacto=Contacto_empresa.objects.all().first()
    redes= Redes_sociales.objects.all().first()
    return render(request,'product-client.html',
                              {'client': client,
                               'galeria_cliente':galeria_cliente,
                               'zatuar':zatuar,
                               'contacto':contacto,
                               'redes':redes,
                      })

def blog(request):
    contexto = {
        'blog': blog_paginado(request),
        'visitas': Visitas_Blog.objects.all(),
        'blogs': Blogs.objects.all().order_by('-id'),
        'categorias': Categoria.objects.all(),
        'paginas': "x" * blog_paginado(request).paginator.num_pages,
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),

    }

    return render(request,"blog-large-image-sidebar-right.html", contexto)


def blogfiltradocategoria(request, n):
    cat = Categoria.objects.get(id=n)
    blogg = Blogs.objects.filter(categoria=cat)
    categorias = Categoria.objects.all()
    zatuar= Zatuar_marca.objects.all().first(),
    contacto= Contacto_empresa.objects.all().first(),
    redes = Redes_sociales.objects.all().first(),
    return render(request,"blog-large-image-sidebar-right.html",
                              {"blogs": blogg, "categorias": cat, "cats": categorias,"zatuar":zatuar,"contacto":contacto,"redes":redes,
                               })


def post(request, n):
    try:
        Visitas_Blog(blog_id=n).save()


    except:
        visita = Visitas_Blog.objects.get(blog_id=n)
        visita.save()
    blogg = Blogs.objects.get(id=n)


    if request.POST:
        if len(request.POST['comment']) > 0:
            pregunta = Comentario(blog=blogg, pregunta=request.POST['comment'], usuario=request.POST['name'],
                                  email=request.POST['email'])
            pregunta.save()
            enviar_email(request, 'Comentarios de Blog', request.POST['name'] + '<' + request.POST['email'] + '>',
                         'zatuar.ec@gmail.com',
                         'Un usuario ha publicado una entrada en el blog, con el texto. >>' + request.POST['comment'])
            enviar_email(request, 'Info Zatuar', 'zatuar.ec@gmail.com',
                         request.POST['name'] + '<' + request.POST['email'] + '>',
                         u'Su comentario fué publicado >>' + request.POST['comment'])
        return HttpResponseRedirect("/post/" + n + "/")
    else:
        preguntas = Comentario.objects.filter(blog=blogg)
        respuestas = Respuesta.objects.all()
        contador = Comentario.objects.all()
    contexto = {
        "zatuar": Zatuar_marca.objects.all().first(),

        "contacto": Contacto_empresa.objects.all().first(),
        "redes": Redes_sociales.objects.all().first(),
        "blog": blogg, "comentarios": preguntas, "respuestas": respuestas, "contador": contador.count(),
        "blogs": Blogs.objects.all().order_by("-fecha")[:20],
    }
    return render(request,"blog-post-sidebar-right.html",contexto)


def postrespuesta(request, n, idBlog):
    if request.POST:
        bloger = Comentario.objects.get(id=n)
        respuesta = Respuesta(comentario=bloger, usuario=request.POST['usuario'], respuesta=request.POST['respuesta'],
                              email=request.POST['email'])
        respuesta.save()
        enviar_email(request, 'Comentarios de Blog', request.POST['usuario'] + '<' + request.POST['email'] + '>',
                     'zatuar.ec@gmail.com',
                     'Un usuario ha publicado una entrada en el blog, con el texto. >>' + request.POST['respuesta'])
        enviar_email(request, 'Info Zatuar', 'zatuar.ec@gmail.com',
                     request.POST['usuario'] + '<' + request.POST['email'] + '>',
                     'Su comentario fué publicado >>' + request.POST['respuesta'])
        return HttpResponseRedirect("/post/" + idBlog + "/")


def error404(request):
    return render(request,"page-404.html")

def contacto(request):
    contexto = {
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
    }
    if request.POST:
        enviar_email(request,request.POST['subject'],request.POST['email'],"zatuar.ec@gmail.com",request.POST['message'],request.POST['name'])
    return render(request,'contact-us.html',contexto)



def enviar_email(request,asunto,from_email,to,mensaje,nombre):
    asunto = asunto
    from_email = from_email
    to = to
    text_content = 'Este mnsaje es importante.'
    html_content = '<p>This is an <strong>important</strong> message.</p>' \
                   '<img src="http://zatuar.com/static/img/zatuar/favizatuar.png"><br>' + mensaje
    msg = EmailMultiAlternatives(asunto, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    # print from_email




