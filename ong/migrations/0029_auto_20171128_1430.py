# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0028_auto_20171128_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='ong/static/images/', verbose_name='foto (utilize este campo para carregar uma nova foto)'),
        ),
    ]