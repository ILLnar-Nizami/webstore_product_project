# Generated by Django 4.2.5 on 2024-09-22 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
