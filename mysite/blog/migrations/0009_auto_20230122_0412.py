# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2023-01-21 22:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20230122_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 21, 22, 42, 1, 818637, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 21, 22, 42, 1, 818125, tzinfo=utc)),
        ),
    ]
