# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0003_auto_20171119_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='atividade_ingles',
            field=models.CharField(max_length=100, null=True, verbose_name='atividade ou função em inglês'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='dataFim',
            field=models.DateField(null=True, verbose_name='data de término das atividades'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='depoimento',
            field=models.TextField(null=True, verbose_name='depoimento'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='depoimento_ingles',
            field=models.TextField(null=True, verbose_name='depoimento em inglês'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='email',
            field=models.EmailField(max_length=100, null=True, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='facebook',
            field=models.CharField(max_length=100, null=True, verbose_name='facebook'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='pais_ingles',
            field=models.CharField(max_length=100, null=True, verbose_name='país em inglês'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='telefone',
            field=models.CharField(max_length=20, null=True, verbose_name='telefone'),
        ),
    ]
