# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20161029_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isFaved',
            field=models.BooleanField(default=False),
        ),
    ]
