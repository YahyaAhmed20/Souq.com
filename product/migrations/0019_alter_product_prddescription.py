# Generated by Django 5.0.1 on 2024-02-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_rename_prdslug_product_prdslug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDdescription',
            field=models.TextField(max_length=500, verbose_name='Product Description'),
        ),
    ]
