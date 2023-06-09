# Generated by Django 4.1.6 on 2023-02-14 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAttributeValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attributevalues', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attributevaluevalues', to='store.productattributevalue')),
                ('productinventory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='productattributevaluevalues', to='store.productinventory')),
            ],
            options={
                'unique_together': {('attributevalues', 'productinventory')},
            },
        ),
    ]
