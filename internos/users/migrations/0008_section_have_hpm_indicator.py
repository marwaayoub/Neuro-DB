# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-03-02 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_section_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='have_hpm_indicator',
            field=models.BooleanField(default=False),
        ),
    ]
