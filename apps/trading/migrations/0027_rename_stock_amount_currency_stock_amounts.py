# Generated by Django 4.2.7 on 2024-01-18 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0026_stock_amount_currency_stock_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency',
            old_name='stock_amount',
            new_name='stock_amounts',
        ),
    ]
