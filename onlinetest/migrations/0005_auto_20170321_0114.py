# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetest', '0004_studentprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
