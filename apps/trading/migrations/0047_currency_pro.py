# Generated by Django 4.2.7 on 2024-01-31 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0046_remove_currency_pro'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='pro',
            field=models.BooleanField(default=True, verbose_name='Pro'),
        ),
    ]
