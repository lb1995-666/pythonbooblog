# Generated by Django 3.2.7 on 2021-10-20 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0055_auto_20211020_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetingroominfo',
            name='time_id',
        ),
    ]