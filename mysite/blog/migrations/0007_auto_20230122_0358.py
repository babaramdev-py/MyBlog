# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2023-01-21 22:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20230122_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 21, 22, 28, 13, 540954, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 21, 22, 28, 13, 540611, tzinfo=utc)),
        ),
    ]
