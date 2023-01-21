# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2023-01-21 22:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20230122_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 21, 22, 43, 16, 831963, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 21, 22, 43, 16, 831439, tzinfo=utc)),
        ),
    ]
