# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-04 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20170504_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
