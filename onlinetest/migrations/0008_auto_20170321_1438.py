# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetest', '0007_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='department',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='institute',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='roll_number',
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='institutionID',
            field=models.CharField(default='None', max_length=50),
        ),
    ]
