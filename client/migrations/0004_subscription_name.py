# Generated by Django 4.2.16 on 2024-09-13 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_client_email_subscription_clients_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='name',
            field=models.CharField(blank=True, help_text='Введите название рассылки', max_length=100, null=True, verbose_name='Названия рассылки'),
        ),
    ]
