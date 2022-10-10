import datetime
from django.db import models


class News(models.Model):
    class Status(models.IntegerChoices):
        created = 1, 'Подготовлена к публикации'
        is_published = 2, 'Опубликована'
        archived = 3, 'В архиве'

    title = models.CharField(
        verbose_name="Название",
        help_text="Введите заголовок новости",
        max_length=255,
    )
    text = models.TextField(
        verbose_name='Текст новости',
        help_text="Введите текст новости",
    )
    status = models.PositiveSmallIntegerField(
        verbose_name="Статус",
        help_text="Введите ",
        choices=Status.choices,
        default=Status.created,
    )
    image = models.ImageField(
        verbose_name="Картинка",
        help_text="Загрузите картинку новости",
        upload_to='news_images/',
        null=True,
        blank=True,
        default=None,
    )
    created = models.DateField(
        verbose_name="Дата создания",
    )
    updated = models.DateField(
        verbose_name="Дата последнего обновления",
        default=None,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.date.today()
        self.updated = datetime.date.today()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-updated']

    def __str__(self):
        return self.title