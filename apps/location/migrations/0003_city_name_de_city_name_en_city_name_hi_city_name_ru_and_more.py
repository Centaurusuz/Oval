# Generated by Django 4.2.7 on 2023-12-19 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_city_use_in_bot'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='name_de',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='city',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='city',
            name='name_hi',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='city',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='city',
            name='name_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_de',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_hi',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
    ]
