# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-03-11 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityinfo', '0072_auto_20190304_1039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indicator',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='activityreport',
            name='form',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='activityreport',
            name='form_category',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='activityreport',
            name='indicator_category',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='activityreport',
            name='indicator_details',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='activityreport',
            name='indicator_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
