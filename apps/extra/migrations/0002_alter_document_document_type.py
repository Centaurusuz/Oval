# Generated by Django 4.2.7 on 2023-12-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_type',
            field=models.CharField(choices=[('privacy_policy', 'Privacy policy'), ('user_agreement', 'User agreement')], max_length=255, verbose_name='Тип документа'),
        ),
    ]
