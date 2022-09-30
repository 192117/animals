from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class OrderPhoto(models.Model):
    CHOICES = {
        'Success': 'Выполнено',
        'Confirmation': 'Подтверждение',
        'Awaiting': 'Ожидание подтверждения',
        'Cancel': 'Отмена',
        'Archive': 'Архив'
    }
    email = models.EmailField(
        verbose_name='Электронная почта заявителя',
        help_text="Введите вашу почту для заявки",
    )
    phone_number = PhoneNumberField(
        verbose_name="Мобильный телефон заявителя",
        help_text="Введите ваш мобильный телефон для связи",
    )
    last_name = models.CharField(
        verbose_name="Фамилия заявителя",
        help_text="Введите вашу фамилию",
        max_length=30,
    )
    first_name = models.CharField(
        verbose_name="Имя заявителя",
        help_text="Введите ваше имя",
        max_length=30,
    )
    body = models.TextField(
        verbose_name="Описание заявки",
        help_text="Введите ваше пожелание",
    )
    status = models.CharField(
        verbose_name='Статус заявки',
        choices=CHOICES,
        default='Awaiting',
        max_length=20
    )


class AddModelAnimal(models.Model):
    pass

class Animals(models.Model):
    pass


