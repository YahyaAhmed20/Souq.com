# Generated by Django 5.0.1 on 2024-02-24 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
