# Generated by Django 4.1.1 on 2022-10-03 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pets_name', models.CharField(help_text='Введите кличку питомца', max_length=30, verbose_name='Кличка питомца')),
                ('photo', models.FileField(help_text='Загрузите фото питомца', upload_to='image_animals/', verbose_name='Фото питомца')),
                ('color', models.CharField(help_text='Введите окрас питомца', max_length=50, verbose_name='Окрас питомца')),
                ('weight', models.DecimalField(decimal_places=2, help_text='Введите вес питомца', max_digits=5, verbose_name='Масса питомца')),
                ('height', models.DecimalField(decimal_places=2, help_text='Введите высотку в холке', max_digits=5, verbose_name='Рост питомца')),
                ('descriptions', models.TextField(help_text='Введите особенности/характер питомца', verbose_name='Особенности/Характер питомца')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='clients.customer')),
            ],
            options={
                'verbose_name': 'Питомец клуба',
                'verbose_name_plural': 'Питомцы клуба',
            },
        ),
    ]
