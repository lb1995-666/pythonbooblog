# Generated by Django 3.2.7 on 2021-10-21 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0059_meetingroominfo_room_use'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetingroominfo',
            name='creator',
        ),
    ]
