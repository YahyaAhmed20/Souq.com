# Generated by Django 5.0.1 on 2024-02-04 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATName', models.CharField(max_length=255, verbose_name='Category Name')),
                ('CATImg', models.ImageField(default='path/to/default/image.jpg', upload_to='Category/%y/%m/%d')),
                ('CATParent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]
