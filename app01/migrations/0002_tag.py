# Generated by Django 3.2.7 on 2021-09-22 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_name', models.CharField(max_length=255)),
                ('app01', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.app01s')),
            ],
        ),
    ]
