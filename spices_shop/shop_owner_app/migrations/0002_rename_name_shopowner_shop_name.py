# Generated by Django 5.0.6 on 2024-05-08 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_owner_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopowner',
            old_name='name',
            new_name='shop_name',
        ),
    ]
