# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-01-16 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityinfo', '0048_indicator_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='label',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='name',
            field=models.CharField(max_length=5000),
        ),
    ]
