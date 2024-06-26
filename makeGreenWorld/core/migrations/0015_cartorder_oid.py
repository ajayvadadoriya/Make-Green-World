# Generated by Django 5.0.1 on 2024-04-07 13:05

import shortuuid.django_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_cartorder_address_cartorder_city_cartorder_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='oid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='123', blank=True, length=4, max_length=30, prefix='sku', unique=True),
        ),
    ]
