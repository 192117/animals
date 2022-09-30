# Generated by Django 4.1.1 on 2022-09-30 08:32

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(help_text='Введите фамилию', max_length=30, verbose_name='Фамилия')),
                ('first_name', models.CharField(help_text='Введите имя', max_length=30, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, help_text='Введите отчество (при наличии)', max_length=30, null=True, verbose_name='Отчество')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Введите ваш мобильный телефон для связи', max_length=128, region=None, verbose_name='Мобильный телефон клиента')),
                ('email', models.EmailField(help_text='Введите вашу почту для заявки', max_length=254, verbose_name='Электронная почта клиента')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
