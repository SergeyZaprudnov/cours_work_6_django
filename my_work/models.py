from django.db import models


class Client(models.Model):  # Модель Клиента
    name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Электронная почта')
    comment = models.CharField(max_length=200, verbose_name='Комментарий')
    is_active = models.BooleanField(default=True, verbose_name='Активность')
