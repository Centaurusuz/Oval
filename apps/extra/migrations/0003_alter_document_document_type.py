# Generated by Django 4.2.7 on 2023-12-19 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0002_alter_document_document_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_type',
            field=models.CharField(choices=[('privacy_policy', 'Privacy policy'), ('user_agreement', 'User agreement'), ('2fauth', '2-factor Authentication')], max_length=255, verbose_name='Тип документа'),
        ),
    ]
