# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0002_auto_20160927_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonenumber',
            name='kind',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
