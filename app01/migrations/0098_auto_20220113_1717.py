# Generated by Django 3.2.7 on 2022-01-13 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0097_auto_20211221_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='head_portrait',
            field=models.ImageField(default=None, upload_to='photo', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 13, 17, 17, 8, 629002), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 13, 17, 17, 8, 626010), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 13, 17, 17, 8, 627007), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='expert',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 13, 17, 17, 8, 628005), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='leavemessage',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 13, 17, 17, 8, 627007), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 13, 17, 17, 8, 624016), verbose_name='创建时间'),
        ),
    ]