# Generated by Django 3.2.7 on 2021-10-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0049_alter_shoporders_buy_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZhanYong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_status', models.CharField(choices=[('use', '占用'), ('no_use', '未占用')], max_length=10, verbose_name='占用状态')),
            ],
        ),
    ]
