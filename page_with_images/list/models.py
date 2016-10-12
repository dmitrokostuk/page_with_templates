# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from mptt.models import TreeForeignKey,MPTTModel
import pytils
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
# Create your models here.

class Catalog(MPTTModel):
    name = models.CharField(verbose_name='name',max_length=256,blank=True  )
    name_slug = models.CharField(verbose_name='Name_slug',max_length=250,blank=True)
    parent = TreeForeignKey('self',null=True,blank=True,related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']
    def __unicode__(self):
        return u"%s %s %s " %(self.name,self.name_slug,self.parent)

    def __str__(self):
        return u"%s %s %s " %(self.name,self.name_slug,self.parent)
    

    def save(self, *args, **kwargs):
        if not self.id:
            self.name_slug = pytils.translit.slugify(self.name)
            return super(Catalog,self).save(**kwargs)

        def get_absolute_url(self):
            return reverse("catalog",kwargs={"slug":self.name_slug})



class Place(models.Model):
     name = models.CharField(verbose_name='Name',max_length=250, blank=True)
     name_slug = models.CharField(verbose_name='Name slug',max_length=250, blank=True)
     description = models.TextField(verbose_name='Description',max_length=250, blank=True)
     cover = models.ImageField(upload_to='journal_cover', verbose_name='Journal cover', blank=True)
     category = models.ManyToManyField(Catalog,
                                      blank=True,
                                      verbose_name='Catalogs')

     def save(self, **kwargs):
        if not self.id:
            self.name_slug = pytils.translit.slugify(self.name)
        return super(Place, self).save(**kwargs)

     @property
     def get_cover(self):
        try:
            return mark_safe('<img src="%s" />' % self.cover.url)
        except:
            return mark_safe('<img src="%s" />' % '/media/journal_cover/plug.jpg')

     def get_absolute_url(self):
       return reverse("place", kwargs={"slug": self.name_slug})


     def __unicode__(self):
        return u"%s %s %s %s %s" %(self.name, self.name_slug, self.description, self.category, self.cover)