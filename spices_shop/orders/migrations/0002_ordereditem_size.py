# Generated by Django 5.0.3 on 2024-04-01 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordereditem',
            name='size',
            field=models.CharField(default='M', max_length=2),
        ),
    ]