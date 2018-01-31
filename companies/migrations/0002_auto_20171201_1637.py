# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='KPP',
        ),
        migrations.RemoveField(
            model_name='company',
            name='OGRN',
        ),
        migrations.RemoveField(
            model_name='company',
            name='OKPO',
        ),
        migrations.AddField(
            model_name='company',
            name='kpp',
            field=models.CharField(default='', max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='ogrn',
            field=models.CharField(default='', max_length=13),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='okpo',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='inn',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='company',
            name='zip_code',
            field=models.CharField(max_length=6),
        ),
    ]