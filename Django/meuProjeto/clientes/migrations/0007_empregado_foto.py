# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20171001_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='empregado',
            name='foto',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
