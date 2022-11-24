# Generated by Django 3.2.7 on 2021-10-22 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0062_overtimeorleave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overtimeorleave',
            name='apply_status',
            field=models.IntegerField(choices=[(0, '审批中'), (1, '同意'), (2, '驳回')], verbose_name='审批状态'),
        ),
        migrations.AlterField(
            model_name='overtimeorleave',
            name='apply_type',
            field=models.IntegerField(choices=[(0, '加班'), (1, '调休')], verbose_name='申请类型'),
        ),
    ]