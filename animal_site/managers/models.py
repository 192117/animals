from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class FunctionsMixin(models.Model):
    function = models.CharField(
        verbose_name="Должность",
        help_text="Введите должность",
        max_length=100,
    )

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.function


class Manager(models.Model):
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
    function = models.ForeignKey(
        FunctionsMixin,
        verbose_name="Должность",
        help_text="Выберите должность из списка. В случае отсутствия необходимой должности, добавьте ее в 'Должности'",
        on_delete=models.CASCADE,
    )
    photo = models.ImageField(
        verbose_name="Фото",
        help_text="Загрузите фото сотрудника",
        upload_to='managers_photo/',
        null=True,
        blank=True,
    )
    phone_number = PhoneNumberField(
        verbose_name="Рабочий телефон",
        help_text="Введите рабочий телефон сотрудника",
    )
    email = models.EmailField(
        verbose_name='Рабочая почта',
        help_text="Введите почту сотрудника",
    )
    welcome_words = models.TextField(
        verbose_name="Приветственное слово",
        help_text="Введите приветственное слово сотрудника",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'
