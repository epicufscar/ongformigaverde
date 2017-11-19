# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 18:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0007_auto_20171119_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampanhaParaDoacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='título')),
                ('descricao', models.TextField(verbose_name='descrição')),
                ('link', models.URLField(blank=True, verbose_name='link para campanha (onde o dinheiro é arrecadado)')),
                ('dataInicio', models.DateField(verbose_name='data de início da campanha')),
                ('dataFim', models.DateField(blank=True, null=True, verbose_name='data de término da campanha (até quando o link fica disponível no site)')),
                ('title', models.CharField(max_length=100, verbose_name='título em inglês')),
                ('description', models.TextField(blank=True, verbose_name='descrição em inglês')),
                ('projeto', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ong.Projeto', verbose_name='projeto para o qual a campanha foi criada')),
            ],
            options={
                'verbose_name': 'campanha para doação',
                'verbose_name_plural': 'campanha para doações',
                'ordering': ['titulo'],
            },
        ),
    ]