# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-19 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_auto_20180119_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='modified',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
