# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-08 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, default='', max_length=50),
        ),
    ]
