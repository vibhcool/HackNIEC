# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-21 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetest', '0006_quesfile_question_studentmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='docs/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='question',
            old_name='questionNo',
            new_name='question_id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='ques_paper_id',
        ),
    ]
