# Generated by Django 3.2.7 on 2022-01-21 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0099_auto_20220120_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 21, 17, 55, 19, 328666), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 21, 17, 55, 19, 329663), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='leavemessage',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 21, 17, 55, 19, 329663), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 21, 17, 55, 19, 326671), verbose_name='创建时间'),
        ),
    ]