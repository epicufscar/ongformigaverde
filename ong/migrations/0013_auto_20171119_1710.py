# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 19:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0012_auto_20171119_1707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='depoimentosobreprojeto',
            options={'ordering': ['projeto__nome'], 'verbose_name': 'depoimento sobre projeto', 'verbose_name_plural': 'depoimentos sobre projeto'},
        ),
    ]
