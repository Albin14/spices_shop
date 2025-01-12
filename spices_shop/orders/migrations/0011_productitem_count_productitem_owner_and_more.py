# Generated by Django 5.0.4 on 2024-05-04 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_remove_productitem_count_remove_productitem_owner_and_more'),
        ('products', '0002_rename_prority_product_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productitem',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='orders.order'),
        ),
        migrations.AddField(
            model_name='productitem',
            name='price_per_unit',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='productitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='added_items', to='products.product'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='quantity',
            field=models.CharField(choices=[('grams', 'Grams'), ('kilos', 'Kilos')], max_length=10),
        ),
    ]
