# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-28 03:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('image_url', models.URLField(verbose_name='图片URL')),
                ('image_upload_path', models.FileField(upload_to='banner/%Y-%m', verbose_name='图片上传路径')),
                ('index', models.CharField(default='10', max_length=10, verbose_name='图片顺序')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verify_code', models.CharField(max_length=20, verbose_name='邮箱验证码')),
                ('send_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间')),
                ('email_address', models.EmailField(max_length=250, verbose_name='邮箱地址')),
                ('send_type', models.CharField(choices=[('Register', '注册'), ('Forget', '忘记密码')], max_length=10, verbose_name='发送类型')),
            ],
            options={
                'verbose_name': '邮箱验证码',
                'verbose_name_plural': '邮箱验证码',
            },
        ),
    ]
