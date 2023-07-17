from django.db import models
from django.urls import reverse


class Client(models.Model):  # Модель Клиента
    name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Электронная почта')
    comment = models.CharField(max_length=200, verbose_name='Комментарий')
    is_active = models.BooleanField(default=True, verbose_name='Активность')

    def get_absolute_url(self):
        return reverse('my_work:user', args=[self.pk])

    def delete(self, **kwargs):
        self.is_active = False
        self.save()

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}, {self.email}, {self.comment}, {self.is_active}'


class Setting(models.Model):
    class Periodicity(models.TextChoices):
        EVERY_DAY = 'Раз в день', 'Раз в день'
        EVERY_WEEK = 'Раз в неделю', 'Раз в неделю'
        EVERY_MONTH = 'Раз в месяц', 'Раз в месяц'

    class Status(models.TextChoices):
        CREATED = 'Создана', 'Создана'
        ACTIVE = 'Активна', 'Активна'
        ENDING = 'Завершена', 'Завершена'

    mailing_name = models.CharField(max_length=150, verbose_name='Название')
