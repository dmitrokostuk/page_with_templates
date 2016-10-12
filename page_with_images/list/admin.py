# _*_ coding: utf-8 _*_
from django.contrib import admin
from .models import Place,Catalog
from mptt.admin import MPTTModelAdmin
# Register your models here.
class CatalogAdmin(MPTTModelAdmin):
    list_display = ('name',)

admin.site.register(Catalog,CatalogAdmin)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ['name']
admin.site.register(Place,PlaceAdmin)