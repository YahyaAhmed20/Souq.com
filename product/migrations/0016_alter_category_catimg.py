# Generated by Django 5.0.1 on 2024-02-07 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_productimage_prdiimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATImg',
            field=models.ImageField(upload_to='Category/%y/%m/%d', verbose_name='Category Image '),
        ),
    ]
