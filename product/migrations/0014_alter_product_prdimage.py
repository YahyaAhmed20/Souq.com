# Generated by Django 5.0.1 on 2024-02-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_product_prdimage_alter_product_prdbrand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDimage',
            field=models.ImageField(blank=True, null=True, upload_to='product/'),
        ),
    ]
