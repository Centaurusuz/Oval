# Generated by Django 4.2.7 on 2024-02-10 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trading', '0053_exchange_fees_withdraw_fees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_type', models.CharField(choices=[('exchange', 'Exchange'), ('withdraw', 'Withdraw'), ('send', 'Send'), ('subscription', 'Subscription'), ('balance_update', 'Balance update')], max_length=255, verbose_name='Тип уведомления')),
                ('foreign_object_id', models.BigIntegerField(default=0, verbose_name='ID внешнего объекта')),
                ('status', models.CharField(choices=[('accepted', 'Accepted'), ('pending', 'Pending'), ('denied', 'Denied')], default='pending', max_length=255, verbose_name='Статус')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('trader', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='trading.trader', verbose_name='Трейдер')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
                'ordering': ['-date'],
            },
        ),
    ]
