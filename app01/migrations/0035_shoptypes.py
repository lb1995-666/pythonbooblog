# Generated by Django 3.2.7 on 2021-10-14 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0034_remove_shops_commodity_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_type_name', models.CharField(blank=True, max_length=255, verbose_name='商品类型名称')),
            ],
        ),
    ]
