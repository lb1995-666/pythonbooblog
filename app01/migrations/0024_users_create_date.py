# Generated by Django 3.2.7 on 2021-10-12 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0023_alter_users_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='create_date',
            field=models.DateField(default=None, verbose_name='创建日期'),
        ),
    ]