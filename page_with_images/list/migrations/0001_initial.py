# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-26 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, verbose_name='Name')),
                ('name_slug', models.CharField(blank=True, max_length=250, verbose_name='Name_slug')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='list.Catalog')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, verbose_name='Name')),
                ('name_slug', models.CharField(blank=True, max_length=250, verbose_name='Name slug')),
                ('description', models.TextField(blank=True, max_length=250, verbose_name='Description')),
                ('cover', models.ImageField(blank=True, upload_to='journal_cover', verbose_name='Journal cover')),
                ('category', models.ManyToManyField(blank=True, to='list.Catalog', verbose_name='Catalogs')),
            ],
        ),
    ]
