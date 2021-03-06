# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-10-31 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityinfo', '0010_auto_20181030_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicatorCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('reporting_level', models.CharField(blank=True, max_length=254, null=True)),
                ('awp_code', models.CharField(blank=True, max_length=254, null=True)),
                ('target', models.PositiveIntegerField(default=0)),
                ('cumulative_results', models.PositiveIntegerField(default=0)),
                ('units', models.CharField(blank=True, max_length=254, null=True)),
                ('status', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
