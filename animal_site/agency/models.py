from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from animal.models import Animals, Category

class OrderAnimal(models.Model):
    CHOICES = (
        ('Success', 'Выполнено'),
        ('Confirmation', 'Подтверждение'),
        ('Awaiting', 'Ожидание подтверждения'),
        ('Cancel', 'Отмена'),
        ('Archive', 'Архив'),
    )
    status = models.CharField(
        verbose_name='Статус заявки',
        choices=CHOICES,
        default='Awaiting',
        max_length=35
    )
    email = models.EmailField(
        verbose_name='Электронная почта заявителя',
        help_text='Введите вашу почту для заявки',
    )
    phone_number = PhoneNumberField(
        verbose_name='Мобильный телефон заявителя',
        help_text='Введите ваш мобильный телефон для связи',
    )
    last_name = models.CharField(
        verbose_name='Фамилия заявителя',
        help_text='Введите вашу фамилию',
        max_length=30,
    )
    first_name = models.CharField(
        verbose_name='Имя заявителя',
        help_text='Введите ваше имя',
        max_length=30,
    )
    animal = models.ForeignKey(
        Animals,
        verbose_name='Выбранное животное',
        help_text='''Выберите животное из списка. В случае отсутствия необходимого животного, оставьте поле пустое 
        и посмотрите выбор категорий''',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    body = models.TextField(
        verbose_name='Описание животного',
        help_text='Введите ваше пожелание, если не получилось выбрать животного из списка имеющихся.',
        blank=True,
        null=True
    )
    class Meta:
        verbose_name = 'Заявка на фотосессию'
        verbose_name_plural = 'Заявки на фотосессии'

    def __str__(self):
        return f'{self.status} {self.email} {self.last_name}'


class AddModelAnimal(models.Model):
    CHOICES = (
        ('Success', 'Выполнено'),
        ('Confirmation', 'Подтверждение'),
        ('Awaiting', 'Ожидание подтверждения'),
        ('Cancel', 'Отмена'),
        ('Archive', 'Архив'),
    )
    status = models.CharField(
        verbose_name='Статус заявки',
        choices=CHOICES,
        default='Awaiting',
        max_length=35
    )
    email = models.EmailField(
        verbose_name='Электронная почта заявителя',
        help_text='Введите вашу почту для заявки',
    )
    phone_number = PhoneNumberField(
        verbose_name='Мобильный телефон заявителя',
        help_text='Введите ваш мобильный телефон для связи',
    )
    last_name = models.CharField(
        verbose_name='Фамилия заявителя',
        help_text='Введите вашу фамилию',
        max_length=30,
    )
    first_name = models.CharField(
        verbose_name='Имя заявителя',
        help_text='Введите ваше имя',
        max_length=30,
    )
    pets_name = models.CharField(
        verbose_name='Кличка питомца',
        help_text='Введите кличку питомца',
        max_length=30,
    )
    photo = models.FileField(
        verbose_name='Фото питомца',
        help_text='Загрузите фото питомца',
        upload_to='image_animals/',
    )
    color = models.CharField(
        verbose_name='Окрас питомца',
        help_text='Введите окрас питомца',
        max_length=50
    )
    weight = models.DecimalField(
        verbose_name='Масса питомца',
        help_text='Введите вес питомца',
        max_digits=5,
        decimal_places=2,
    )
    height = models.DecimalField(
        verbose_name='Рост питомца',
        help_text='Введите высотку в холке',
        max_digits=5,
        decimal_places=2,
    )
    descriptions = models.TextField(
        verbose_name='Особенности/Характер питомца',
        help_text='Введите особенности/характер питомца',
    )
    class Meta:
        verbose_name = 'Заявка на вступление в клуб'
        verbose_name_plural = 'Заявки на вступление в клуб'

    def __str__(self):
        return f'{self.status} {self.email} {self.last_name}'


