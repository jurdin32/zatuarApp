from django import template

from Blogs.models import Visitas_Blog
register=template.Library()

@register.simple_tag
def vistanumero(id):
    numero=0
    try:
        numero=Visitas_Blog.objects.get(blog_id=id).visita
    except:
        numero=0
    return numero

