# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-29 16:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20171201_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='modified',
            field=models.DateField(default=datetime.datetime(2017, 12, 29, 16, 43, 42, 91231, tzinfo=utc)),
        ),
    ]
