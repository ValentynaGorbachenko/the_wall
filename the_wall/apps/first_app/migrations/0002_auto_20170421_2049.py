# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
