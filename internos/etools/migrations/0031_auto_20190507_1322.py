# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-07 13:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_office'),
        ('etools', '0030_partnerorganization_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.Office'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.Section'),
        ),
    ]
