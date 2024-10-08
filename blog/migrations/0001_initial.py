# Generated by Django 4.2.16 on 2024-09-13 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержимое статьи')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/photo', verbose_name='Изображение')),
                ('views_counter', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
