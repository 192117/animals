from django.db import models
from django.urls import reverse
from animal_site.utils import translite
from clients.models import Customer

class Animals(models.Model):
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
    class Meta:
        verbose_name = "Питомец клуба"
        verbose_name_plural = "Питомцы клуба"

    def __str__(self):
        return f'{self.pets_name} {self.descriptions}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = translite(self.pets_name+self.color+str(self.owner))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('animal_detail_url', kwargs={'slug': self.slug})