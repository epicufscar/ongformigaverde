# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0019_auto_20171119_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='membro',
            name='idade',
            field=models.IntegerField(blank=True, default=0, verbose_name='idade'),
            preserve_default=False,
        ),
    ]
