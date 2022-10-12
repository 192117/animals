# Generated by Django 4.1.1 on 2022-10-12 11:50

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddModelAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Success', 'Выполнено'), ('Confirmation', 'Подтверждение'), ('Awaiting', 'Ожидание подтверждения'), ('Cancel', 'Отмена'), ('Archive', 'Архив')], default='Awaiting', max_length=35, verbose_name='Статус заявки')),
                ('email', models.EmailField(help_text='Введите вашу почту для заявки', max_length=254, verbose_name='Электронная почта заявителя')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Введите ваш мобильный телефон для связи', max_length=128, region=None, verbose_name='Мобильный телефон заявителя')),
                ('last_name', models.CharField(help_text='Введите вашу фамилию', max_length=30, verbose_name='Фамилия заявителя')),
                ('first_name', models.CharField(help_text='Введите ваше имя', max_length=30, verbose_name='Имя заявителя')),
                ('pets_name', models.CharField(help_text='Введите кличку питомца', max_length=30, verbose_name='Кличка питомца')),
                ('photo', models.FileField(help_text='Загрузите фото питомца', upload_to='image_animals/', verbose_name='Фото питомца')),
                ('color', models.CharField(help_text='Введите окрас питомца', max_length=50, verbose_name='Окрас питомца')),
                ('weight', models.DecimalField(decimal_places=2, help_text='Введите вес питомца', max_digits=5, verbose_name='Масса питомца')),
                ('height', models.DecimalField(decimal_places=2, help_text='Введите высотку в холке', max_digits=5, verbose_name='Рост питомца')),
                ('descriptions', models.TextField(help_text='Введите особенности/характер питомца', verbose_name='Особенности/Характер питомца')),
            ],
            options={
                'verbose_name': 'Заявка на вступление в клуб',
                'verbose_name_plural': 'Заявки на вступление в клуб',
            },
        ),
        migrations.CreateModel(
            name='OrderAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Success', 'Выполнено'), ('Confirmation', 'Подтверждение'), ('Awaiting', 'Ожидание подтверждения'), ('Cancel', 'Отмена'), ('Archive', 'Архив')], default='Awaiting', max_length=35, verbose_name='Статус заявки')),
                ('email', models.EmailField(help_text='Введите вашу почту для заявки', max_length=254, verbose_name='Электронная почта заявителя')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Введите ваш мобильный телефон для связи', max_length=128, region=None, verbose_name='Мобильный телефон заявителя')),
                ('last_name', models.CharField(help_text='Введите вашу фамилию', max_length=30, verbose_name='Фамилия заявителя')),
                ('first_name', models.CharField(help_text='Введите ваше имя', max_length=30, verbose_name='Имя заявителя')),
                ('body', models.TextField(blank=True, help_text='Введите ваше пожелание, если не получилось выбрать животного из списка имеющихся.', null=True, verbose_name='Описание животного')),
                ('animal', models.ForeignKey(blank=True, help_text='Выберите животное из списка. В случае отсутствия необходимого животного, оставьте поле пустое \n        и посмотрите выбор категорий', null=True, on_delete=django.db.models.deletion.CASCADE, to='animal.animals', verbose_name='Выбранное животное')),
                ('category', models.ForeignKey(blank=True, help_text='Выберите категорию из списка. Если не выбрали животное, в случае отсутствия необходимой категории, \n        оставьте поле пустое и переходите к описанию животного, которое вы бы хотели', null=True, on_delete=django.db.models.deletion.CASCADE, to='animal.category', verbose_name='Выбранная категория')),
            ],
            options={
                'verbose_name': 'Заявка на фотосессию',
                'verbose_name_plural': 'Заявки на фотосессии',
            },
        ),
    ]
