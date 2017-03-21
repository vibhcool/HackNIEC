# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 19:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetest', '0003_auto_20170320_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('roll_number', models.CharField(max_length=20)),
                ('institute', models.CharField(max_length=128)),
                ('department', models.CharField(max_length=64)),
                ('created_time', models.DateTimeField(default=datetime.datetime(2017, 3, 20, 19, 42, 27, 8478, tzinfo=utc))),
            ],
        ),
    ]
