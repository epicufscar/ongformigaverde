# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0017_auto_20171119_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='data de postagem')),
                ('titulo', models.CharField(max_length=100, verbose_name='título da notícia')),
                ('texto', models.TextField(verbose_name='texto da notícia')),
                ('link', models.URLField(blank=True, verbose_name='link para conteúdo externo (Exemplo: post no Facebook)')),
            ],
            options={
                'verbose_name': 'notícia',
                'verbose_name_plural': 'notícias',
            },
        ),
        migrations.RemoveField(
            model_name='receitadedoacoes',
            name='comments',
        ),
        migrations.AlterField(
            model_name='receitadedoacoes',
            name='comentarios',
            field=models.CharField(blank=True, max_length=100, verbose_name='outras informações, se houver (Exemplo: nome do projeto ou evento para o qual o valor foi utilizado)'),
        ),
    ]