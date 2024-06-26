# Generated by Django 5.0.1 on 2024-01-24 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_product_life_product_stock_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='price',
            field=models.DecimalField(decimal_places=4, default='1.99', max_digits=11),
        ),
        migrations.AlterField(
            model_name='cartorderitems',
            name='price',
            field=models.DecimalField(decimal_places=4, default='1.99', max_digits=11),
        ),
        migrations.AlterField(
            model_name='cartorderitems',
            name='total',
            field=models.DecimalField(decimal_places=4, default='1.99', max_digits=11),
        ),
        migrations.AlterField(
            model_name='product',
            name='life',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(decimal_places=4, default='2.99', max_digits=11),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=4, default='1.99', max_digits=11),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_count',
            field=models.CharField(default='100', max_length=100),
        ),
    ]
