# Generated by Django 3.2.7 on 2021-10-09 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0021_auto_20211009_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.IntegerField(verbose_name='手机号'),
        ),
    ]