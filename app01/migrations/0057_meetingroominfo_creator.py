# Generated by Django 3.2.7 on 2021-10-21 02:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app01', '0056_remove_meetingroominfo_time_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingroominfo',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]