# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0041_auto_20171128_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='apagarPhoto',
            field=models.BooleanField(default=False, help_text='Marque esta opção apenas se deseja excluir a foto de capa ao salvar', verbose_name='excluir foto de capa?'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='dataFim',
            field=models.DateField(blank=True, help_text='Preencher, se houver', null=True, verbose_name='data de término do projeto'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='membros',
            field=models.ManyToManyField(blank=True, help_text='Membros responsáveis pelo projeto, se houver', to='ong.Membro', verbose_name='membros'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='parceiros',
            field=models.ManyToManyField(blank=True, help_text='Parceiros envolvidos com o projeto, se houver', to='ong.Parceria', verbose_name='parceiros'),
        ),
    ]
