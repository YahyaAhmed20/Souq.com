# Generated by Django 5.0.1 on 2024-02-04 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_prdimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='PRDimage',
        ),
    ]