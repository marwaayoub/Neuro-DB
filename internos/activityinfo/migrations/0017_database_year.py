# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-12-07 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityinfo', '0016_auto_20181207_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='year',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
