# Generated by Django 3.2.7 on 2022-02-05 02:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0103_auto_20220205_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 10, 58, 38, 14887), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 10, 58, 38, 15695), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='leavemessage',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 10, 58, 38, 16452), verbose_name='创建时间'),
        ),
    ]
