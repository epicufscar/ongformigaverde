# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 18:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0045_auto_20171128_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campanhaparadoacoes',
            name='projeto',
            field=models.ForeignKey(blank=True, help_text='Projeto para o qual a campanha foi criada, se aplicável', on_delete=django.db.models.deletion.CASCADE, to='ong.Projeto', verbose_name='projeto'),
        ),
    ]
