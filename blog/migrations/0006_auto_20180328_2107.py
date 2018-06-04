# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-29 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'get_latest_by': 'modified', 'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='link',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='link',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]