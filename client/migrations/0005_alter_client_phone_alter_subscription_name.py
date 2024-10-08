# Generated by Django 4.2.16 on 2024-09-13 08:16

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_subscription_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Введите номер телефона', max_length=31, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='name',
            field=models.CharField(blank=True, help_text='Введите название рассылки', max_length=100, null=True, verbose_name='Название рассылки'),
        ),
    ]
