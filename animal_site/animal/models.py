from django.db import models
from django.urls import reverse
from animal_site.utils import translite
from clients.models import Customer
import random

class Category(models.Model):
    name = models.CharField(
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
        max_length=100,
    )
    photo = models.FileField(
        verbose_name='Фото категории',
        help_text='Загрузите фото категории',
        upload_to='agency/',
    )

    class Meta:
        verbose_name = "Категория животного"
        verbose_name_plural = "Категории животного"

        def __str__(self):
            return f'{self.name}'

class Animals(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='animals',
    )
    pets_name = models.CharField(
        verbose_name="Кличка питомца",
        help_text="Введите кличку питомца",
        max_length=30,
    )
    photo = models.FileField(
        verbose_name='Фото питомца',
        help_text='Загрузите фото питомца',
        upload_to='image_animals/',
    )
    color = models.CharField(
        verbose_name="Окрас питомца",
        help_text="Введите окрас питомца",
        max_length=50
    )
    weight = models.DecimalField(
        verbose_name="Масса питомца",
        help_text="Введите вес питомца",
        max_digits=5,
        decimal_places=2,
    )
    height = models.DecimalField(
        verbose_name="Рост питомца",
        help_text="Введите высотку в холке",
        max_digits=5,
        decimal_places=2,
    )
    descriptions = models.TextField(
        verbose_name="Особенности/Характер питомца",
        help_text="Введите особенности/характер питомца",
    )
    owner = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='pets',
    )
    slug = models.SlugField(
        max_length=150,
        blank=True,
        unique=True
    )
    rate = models.IntegerField(
        default=0
    )
    class Meta:
        verbose_name = "Питомец клуба"
        verbose_name_plural = "Питомцы клуба"

    def __str__(self):
        return f'{self.pets_name}'

    def save(self, *args, **kwargs):
        while True:
            try:
                number = str(random.random()).split('.')[-1]
                self.slug = translite(self.pets_name+'_'+number[:random.randrange(1, len(number))])
                break
            except Exception:
                pass
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('animal_detail_url', kwargs={'slug': self.slug})