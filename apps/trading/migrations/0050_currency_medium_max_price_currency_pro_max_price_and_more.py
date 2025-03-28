# Generated by Django 4.2.7 on 2024-02-01 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0049_remove_currency_medium_max_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='medium_max_price',
            field=models.FloatField(default=0, verbose_name='Medium max price'),
        ),
        migrations.AddField(
            model_name='currency',
            name='pro_max_price',
            field=models.FloatField(default=0, verbose_name='Pro max price'),
        ),
        migrations.AddField(
            model_name='currency',
            name='simple_max_price',
            field=models.FloatField(default=0, verbose_name='Simple max price'),
        ),
    ]
