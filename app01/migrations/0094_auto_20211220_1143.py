# Generated by Django 3.2.7 on 2021-12-20 03:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0093_auto_20211220_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='account_date',
            field=models.DateField(verbose_name='账单日期'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 20, 11, 43, 1, 347595), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='income_expenses',
            field=models.IntegerField(choices=[(0, '收入'), (1, '支出')], verbose_name='收支'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='income_type',
            field=models.IntegerField(choices=[(0, '薪资'), (1, '其他')], verbose_name='收入类型'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='spending_type',
            field=models.IntegerField(choices=[(0, '交通'), (1, '餐饮'), (2, '红包'), (3, '娱乐'), (4, '其他')], verbose_name='支出类型'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 20, 11, 43, 1, 345600), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 20, 11, 43, 1, 345600), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='expert',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 20, 11, 43, 1, 346598), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='leavemessage',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 20, 11, 43, 1, 346598), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 20, 11, 43, 1, 343605), verbose_name='创建时间'),
        ),
    ]
