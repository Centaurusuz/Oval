# Generated by Django 4.2.7 on 2024-02-08 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0009_subscription_type_is_popular'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription_feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='Очередь')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('status', models.CharField(choices=[('active', 'active'), ('deactive', 'deactive')], default='active', max_length=255, verbose_name='Статус')),
                ('subscription_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='subscription.subscription_type', verbose_name='Тип подписки')),
            ],
            options={
                'verbose_name': 'Subscription_feature',
                'verbose_name_plural': 'Subscription_features',
                'ordering': ['subscription_type', 'order'],
            },
        ),
    ]
