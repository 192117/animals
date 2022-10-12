from django.db import models


class Info(models.Model):
    about_article = models.TextField(
        verbose_name='Информация о нас',
        help_text='Введите информацию, которая будет отображаться в шапке на главной. 250 символов максимум.',
        max_length=250
    )
    about_footer = models.TextField(
        verbose_name='Информация о нас',
        help_text='Введите информацию, которая будет отображаться внизу страниц, в футере. 50 символов максимум.',
        max_length=50
    )
    about_body = models.TextField(
        verbose_name='Информация о нас',
        help_text='Введите информацию, которая будет отображаться на странице о компании. 500 символов максимум.',
        max_length=500
    )
    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информации"

    def __str__(self):
        return f'{self.about_footer}'


class Questions(models.Model):
    question = models.TextField(
        verbose_name='Вопрос в FAQ',
        help_text='Введите вопрос, который будет отображаться в FAQ. 50 символов максимум.',
        max_length=50
    )

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return f'{self.question}'


class Answers(models.Model):
    answer = models.TextField(
        verbose_name='Ответ на вопрос в FAQ',
        help_text='Введите ответ на вопрос, который будет отображаться в FAQ. 500 символов максимум.',
        max_length=500
    )
    question = models.ForeignKey(
        Questions,
        on_delete=models.CASCADE,
        related_name='answer'
    )

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return f'{self.answer}'


class PriceList(models.Model):
    price_pdf = models.FileField(
        verbose_name='Прайс лист',
        help_text='Прикрепите прайс лист',
        upload_to='price_doc/'
    )

    class Meta:
        verbose_name = "Прайс лист"
        verbose_name_plural = "Прайс листы"

    def __str__(self):
        return f'{self.price_pdf}'


class SocialMedia(models.Model):
    telegram = models.CharField(
        verbose_name='Ссылка на телеграмм',
        help_text='Вставьте ссылку на телеграмм',
        max_length=50
    )
    vk = models.CharField(
        verbose_name='Ссылка на вконтакте',
        help_text='Вставьте ссылку на вконтакте',
        max_length=50
    )
    whatsapp = models.CharField(
        verbose_name='Ссылка на whatsapp',
        help_text='Вставьте ссылку на whatsapp',
        max_length=50
    )

    class Meta:
        verbose_name = "Соцсети"
        verbose_name_plural = "Соцсети"

    def __str__(self):
        return f'соцсети'