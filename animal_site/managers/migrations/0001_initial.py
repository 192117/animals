# Generated by Django 4.1.1 on 2022-10-13 07:10

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionsMixin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function', models.CharField(help_text='Введите должность', max_length=100, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(help_text='Введите фамилию', max_length=30, verbose_name='Фамилия')),
                ('first_name', models.CharField(help_text='Введите имя', max_length=30, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, help_text='Введите отчество (при наличии)', max_length=30, null=True, verbose_name='Отчество')),
                ('photo', models.ImageField(blank=True, help_text='Загрузите фото сотрудника', null=True, upload_to='managers_photo/', verbose_name='Фото')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Введите рабочий телефон сотрудника', max_length=128, region=None, verbose_name='Рабочий телефон')),
                ('email', models.EmailField(help_text='Введите почту сотрудника', max_length=254, verbose_name='Рабочая почта')),
                ('welcome_words', models.TextField(blank=True, help_text='Введите приветственное слово сотрудника', null=True, verbose_name='Приветственное слово')),
                ('function', models.ForeignKey(help_text="Выберите должность из списка. В случае отсутствия необходимой должности, добавьте ее в 'Должности'", on_delete=django.db.models.deletion.CASCADE, to='managers.functionsmixin', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
