# Generated by Django 4.1.6 on 2023-03-30 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='product_image/default.png', upload_to='product_image/'),
        ),
        migrations.AlterField(
            model_name='media',
            name='img_url',
            field=models.ImageField(default='product_image/default.png', help_text='format: required, default-default.png', upload_to='product_image/', verbose_name='product image'),
        ),
    ]
