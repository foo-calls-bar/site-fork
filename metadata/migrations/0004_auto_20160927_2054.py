# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 01:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0003_phonenumber_kind'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='site',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
