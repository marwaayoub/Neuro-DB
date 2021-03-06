# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-02-25 14:59
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activityinfo', '0065_activityreportlive'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='cumulative_values_live',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True),
        ),
        migrations.AddField(
            model_name='indicator',
            name='values_gov_live',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True),
        ),
        migrations.AddField(
            model_name='indicator',
            name='values_live',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True),
        ),
        migrations.AddField(
            model_name='indicator',
            name='values_partners_gov_live',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True),
        ),
        migrations.AddField(
            model_name='indicator',
            name='values_partners_live',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True),
        ),
    ]
