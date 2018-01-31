# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-26 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_remove_creditlimit_insurer'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='insurer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='companies.Insurer'),
            preserve_default=False,
        ),
    ]