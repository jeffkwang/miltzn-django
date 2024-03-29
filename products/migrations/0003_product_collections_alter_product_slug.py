# Generated by Django 5.0.1 on 2024-02-02 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='collections',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
