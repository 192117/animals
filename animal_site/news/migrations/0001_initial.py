# Generated by Django 4.1.1 on 2022-10-13 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите заголовок новости', max_length=255, unique=True, verbose_name='Название')),
                ('text', models.TextField(help_text='Введите текст новости', verbose_name='Текст новости')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Подготовлена к публикации'), (2, 'Опубликована'), (3, 'В архиве')], default=1, help_text='Введите ', verbose_name='Статус')),
                ('image', models.ImageField(blank=True, default=None, help_text='Загрузите картинку новости', null=True, upload_to='news_images/', verbose_name='Картинка')),
                ('created', models.DateField(verbose_name='Дата создания')),
                ('updated', models.DateField(blank=True, default=None, null=True, verbose_name='Дата последнего обновления')),
                ('slug', models.SlugField(blank=True, max_length=150)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-updated'],
            },
        ),
    ]
