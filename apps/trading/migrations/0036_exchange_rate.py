# Generated by Django 4.2.7 on 2024-01-24 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0035_alter_rate_template_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange',
            name='rate',
            field=models.FloatField(default=0, verbose_name='Курс'),
        ),
    ]
