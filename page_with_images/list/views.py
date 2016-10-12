# _*_ coding: utf-8 _*_
from django.shortcuts import render
from .models import Catalog,Place
# Create your views here
#
# .

def catalog_show(request,id):
    catalog = Catalog.objects.get(pk=id)
    places = Place.objects.filter(category = catalog).all()
    return render(request,'catalog_show.html',{'catalog':catalog, 'places': places})

def home_page(request):
    places = Place.objects.all()

    return render(request,'list.html',{'places':places,'nodes' :Catalog.objects.all()})

def place(request,slug=None):
    place = Place.objects.all()
    return render(request,'place.html',{'place':place })
