# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0040_auto_20171128_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parceria',
            name='telefone',
            field=models.CharField(blank=True, help_text='Telefone principal para contato com o parceiro', max_length=20, verbose_name='telefone do parceiro'),
        ),
    ]
