# _*_ coding: utf-8 _*_
from django import templatetags,template
from ..models import Catalog
register = template.Library()

@register.inclusion_tag("menu.html")

def menu():
    out = {}
    catagory = Catalog.objects.all()
    out['items'] = catagory
    return out