# Generated by Django 4.2.7 on 2024-01-06 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0019_alter_exchange_exchange_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='trader',
            name='bot_registration_finished',
            field=models.BooleanField(default=False, verbose_name='Завершил регистрацию'),
        ),
    ]
