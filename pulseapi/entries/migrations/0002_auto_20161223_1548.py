# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-23 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='internal_notes',
            field=models.TextField(blank=True),
        ),
    ]
