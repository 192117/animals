from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    CHOICES = (
        ('Breeder', 'Заводчик'),
        ('Client', 'Клиент'),
    )
    role = models.CharField(
        verbose_name='Тип клиента',
        choices=CHOICES,
        default='Breeder',
        max_length=35
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        help_text="Введите фамилию",
        max_length=30,
    )
    first_name = models.CharField(
        verbose_name="Имя",
        help_text="Введите имя",
        max_length=30,
    )
    patronymic = models.CharField(
        verbose_name="Отчество",
        help_text="Введите отчество (при наличии)",
        max_length=30,
        null=True,
        blank=True,
    )
    phone_number = PhoneNumberField(
        verbose_name="Мобильный телефон клиента",
        help_text="Введите ваш мобильный телефон для связи",
    )
    email = models.EmailField(
        verbose_name='Электронная почта клиента',
        help_text="Введите вашу почту для заявки",
    )
    review = models.TextField(
        verbose_name='Отзыв',
        help_text='Введите отзыва',
        null=True,
        blank=True,
    )
    photo_client = models.FileField(
        verbose_name='Фото клиента',
        help_text='Загрузите свое фото',
        upload_to='image_clients/',
    )
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f'{self.last_name} {self.first_name}'