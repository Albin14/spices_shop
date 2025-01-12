# Generated by Django 5.0.4 on 2024-05-04 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_productitem_price_per_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productitem',
            name='count',
        ),
        migrations.RemoveField(
            model_name='productitem',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='productitem',
            name='price_per_unit',
        ),
        migrations.RemoveField(
            model_name='productitem',
            name='product',
        ),
        migrations.AlterField(
            model_name='productitem',
            name='quantity',
            field=models.IntegerField(choices=[(100, '100 grams'), (250, '250 grams'), (500, '500 grams'), (1000, '1 kilogram')]),
        ),
    ]
