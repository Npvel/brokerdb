# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-26 16:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0008_auto_20180126_1925'),
        ('customers', '0002_contract_insurer'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditLimit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField()),
                ('requested_amount', models.IntegerField()),
                ('approved_date', models.DateField()),
                ('approved_amount', models.IntegerField()),
                ('expiration_date', models.DateField(null=True)),
                ('guarantor_comment', models.TextField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Insurer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
            ],
        ),
        migrations.AlterField(
            model_name='contract',
            name='insurer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Insurer'),
        ),
        migrations.AddField(
            model_name='creditlimit',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Contract'),
        ),
        migrations.AddField(
            model_name='creditlimit',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Currency'),
        ),
        migrations.AddField(
            model_name='creditlimit',
            name='debitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company'),
        ),
        migrations.AddField(
            model_name='creditlimit',
            name='guarantor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='granted_limits', to='companies.Company'),
        ),
    ]
