# Generated by Django 4.2.7 on 2023-12-20 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_city_name_de_city_name_en_city_name_hi_city_name_ru_and_more'),
        ('trading', '0009_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trader',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='location.city'),
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_input', models.IntegerField(default=0, verbose_name='Количество ввода')),
                ('amount_output', models.IntegerField(default=0, verbose_name='Количество выхода')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('currency_from', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='currency_from', to='trading.currency', verbose_name='Валюта (из)')),
                ('currency_to', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='currency_to', to='trading.currency', verbose_name='Валюта (в)')),
                ('trader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading.trader', verbose_name='Трейдер')),
            ],
            options={
                'verbose_name': 'Обмен',
                'verbose_name_plural': 'Обмены',
                'ordering': ['id'],
            },
        ),
    ]
