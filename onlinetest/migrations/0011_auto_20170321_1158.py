# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-21 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetest', '0010_merge_20170321_1105'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AlterField(
            model_name='quesfile',
            name='ques_paper_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]