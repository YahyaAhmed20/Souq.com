# Generated by Django 5.0.1 on 2024-02-04 19:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_category_catdescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATParent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CATParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
    ]