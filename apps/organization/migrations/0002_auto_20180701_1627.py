# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-01 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='work_year',
            field=models.IntegerField(verbose_name='工龄'),
        ),
    ]
