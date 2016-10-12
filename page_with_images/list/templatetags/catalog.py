# _*_ coding: utf-8 _*_
from django import template,templatetags
from ..models import Catalog

register = template.Library()

@register.inclusion_tag("catalog.html")
def catalog():
    out = {}
    nodes = Catalog.objects.all()
    out['nodes'] = catalog
    return out