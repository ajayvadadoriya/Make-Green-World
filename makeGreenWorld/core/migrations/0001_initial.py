# Generated by Django 5.0.1 on 2024-01-19 11:41

import core.models
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Addesse',
            },
        ),
        migrations.CreateModel(
            name='CartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default='1.99', max_digits=4)),
                ('paid_status', models.BooleanField(default=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('product_status', models.CharField(choices=[('process', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='process', max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Cart Order',
            },
        ),
        migrations.CreateModel(
            name='CartOrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(max_length=200)),
                ('product_status', models.CharField(max_length=200)),
                ('item', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('qty', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default='1.99', max_digits=4)),
                ('total', models.DecimalField(decimal_places=2, default='1.99', max_digits=4)),
            ],
            options={
                'verbose_name_plural': 'Cart Order Items',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=30, prefix='cat', unique=True)),
                ('title', models.CharField(default='Food', max_length=100)),
                ('image', models.ImageField(default='category.jpg', upload_to='category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=30, prefix='', unique=True)),
                ('title', models.CharField(default='Fresh Pear', max_length=100)),
                ('image', models.ImageField(default='product.jpg', upload_to=core.models.user_directory_path)),
                ('description', models.TextField(blank=True, default='This is the product', null=True)),
                ('price', models.DecimalField(decimal_places=2, default='1.99', max_digits=4)),
                ('old_price', models.DecimalField(decimal_places=2, default='2.99', max_digits=4)),
                ('specification', models.TextField(blank=True, null=True)),
                ('product_status', models.CharField(choices=[('draft', 'Draft'), ('disabled', 'Disabled'), ('rejected', 'Rejected'), ('in_review', 'In Review'), ('published', 'Published')], default='in_review', max_length=10)),
                ('status', models.BooleanField(default=True)),
                ('in_stock', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('digital', models.BooleanField(default=False)),
                ('sku', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=4, max_length=30, prefix='sku', unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='product.jpg', upload_to='product-images')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating', models.TextField(choices=[('1', '★'), ('2', '★★'), ('3', '★★★'), ('4', '★★★★'), ('5', '★★★★★')], default=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Product Reviews',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=30, prefix='Ven', unique=True)),
                ('title', models.CharField(default='Nestify', max_length=100)),
                ('image', models.ImageField(default='Vendor.jpg', upload_to=core.models.user_directory_path)),
                ('description', models.TextField(blank=True, default='I  am vendor', null=True)),
                ('address', models.CharField(default='Ahmedabad', max_length=100)),
                ('contact', models.CharField(default='+123(555) 555', max_length=100)),
                ('chat_resp_time', models.CharField(default='100', max_length=100)),
                ('shipping_on_time', models.CharField(default='100', max_length=100)),
                ('authentic_rating', models.CharField(default='100', max_length=100)),
                ('days_return', models.CharField(default='100', max_length=100)),
                ('warranty_period', models.CharField(default='100', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Vendors',
            },
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'wishlists',
            },
        ),
    ]