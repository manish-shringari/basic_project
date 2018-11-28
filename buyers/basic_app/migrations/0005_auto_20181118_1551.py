# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-11-18 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_auto_20181103_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='vin_num',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
