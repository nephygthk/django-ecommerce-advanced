# Generated by Django 4.1.6 on 2023-02-14 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_productattributevalues'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinventory',
            name='attribute_values',
            field=models.ManyToManyField(related_name='product_attribute_values', through='store.ProductAttributeValues', to='store.productattributevalue'),
        ),
    ]
