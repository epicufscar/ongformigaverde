# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0011_depoimentoparaprojeto'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepoimentoSobreProjeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome de quem fez o depoimento')),
                ('idade', models.PositiveIntegerField(blank=True, verbose_name='idade de quem fez o depoimento')),
                ('depoimento', models.TextField(verbose_name='depoimento')),
                ('linkVideo', models.URLField(blank=True, verbose_name='link para depoimento em vídeo')),
                ('statement', models.TextField(blank=True, verbose_name='[INGLÊS] Depoimento em inglês')),
            ],
            options={
                'verbose_name': 'depoimento sobre projeto',
                'verbose_name_plural': 'depoimentos sobre projeto',
                'ordering': ['projeto'],
            },
        ),
        migrations.RemoveField(
            model_name='depoimentoparaprojeto',
            name='projeto',
        ),
        migrations.AlterField(
            model_name='campanhaparadoacoes',
            name='description',
            field=models.TextField(blank=True, verbose_name='[INGLÊS] Descrição em inglês'),
        ),
        migrations.AlterField(
            model_name='campanhaparadoacoes',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ong.Projeto', verbose_name='projeto para o qual a campanha foi criada'),
        ),
        migrations.AlterField(
            model_name='campanhaparadoacoes',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='[INGLÊS] Título em inglês'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='activity',
            field=models.CharField(blank=True, max_length=100, verbose_name='[INGLÊS] Atividade ou função em inglês'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='country',
            field=models.CharField(blank=True, max_length=100, verbose_name='[INGLÊS] País em inglês'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='statement',
            field=models.TextField(blank=True, verbose_name='[INGLÊS] Depoimento em inglês'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='description',
            field=models.TextField(blank=True, verbose_name='[INGLÊS] Descrição em inglês'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='[INGLÊS] Nome em inglês'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='public',
            field=models.CharField(blank=True, choices=[('E1', 'CHILDREN'), ('E2', 'ADULTS'), ('E3', 'EVERYONE')], max_length=2, verbose_name='[INGLÊS] Público alvo em inglês'),
        ),
        migrations.DeleteModel(
            name='DepoimentoParaProjeto',
        ),
        migrations.AddField(
            model_name='depoimentosobreprojeto',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ong.Projeto', verbose_name='projeto para o qual o depoimento foi feito'),
        ),
    ]
