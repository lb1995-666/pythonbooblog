# Generated by Django 3.2.7 on 2022-01-20 03:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0098_auto_20220113_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.DeleteModel(
            name='Bill',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Expert',
        ),
        migrations.RemoveField(
            model_name='identity',
            name='user',
        ),
        migrations.DeleteModel(
            name='ImgPath',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='app01',
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='comment_head_portrait',
            field=models.CharField(default='photo/default_head_portrait.jpg', max_length=255, verbose_name='评论者头像地址'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 11, 45, 5, 419138), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 11, 45, 5, 420165), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='leavemessage',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 11, 45, 5, 420165), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 11, 45, 5, 417172), verbose_name='创建时间'),
        ),
        migrations.DeleteModel(
            name='App01s',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Identity',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]