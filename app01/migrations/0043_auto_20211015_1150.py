# Generated by Django 3.2.7 on 2021-10-15 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0042_auto_20211015_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity_name', models.CharField(blank=True, max_length=255, verbose_name='商品名称')),
                ('commodity_price', models.CharField(blank=True, max_length=255, verbose_name='商品单价')),
                ('buy_commodity_num', models.CharField(blank=True, max_length=255, verbose_name='购买商品数量')),
                ('buy_total_price', models.CharField(blank=True, max_length=255, verbose_name='购买商品总价')),
                ('buy_user', models.CharField(blank=True, max_length=255, verbose_name='购买人')),
                ('buy_user_phone', models.CharField(blank=True, max_length=255, verbose_name='购买人手机号')),
            ],
        ),
        migrations.AlterField(
            model_name='shops',
            name='commodity_presentation',
            field=models.TextField(default=None, max_length=2048, verbose_name='商品描述'),
        ),
    ]
