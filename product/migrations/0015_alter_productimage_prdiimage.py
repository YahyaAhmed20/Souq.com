# Generated by Django 5.0.1 on 2024-02-07 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_product_prdimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='PRDIimage',
            field=models.ImageField(blank=True, null=True, upload_to='product/'),
        ),
    ]
