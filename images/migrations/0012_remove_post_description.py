# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 10:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0011_auto_20161119_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
    ]
