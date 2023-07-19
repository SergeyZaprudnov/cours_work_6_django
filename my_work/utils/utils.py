from django.conf import settings
from django.core.mail import send_mail
from django.utils.timezone import now

from apscheduler.schedulers.background import BackgroundScheduler

from my_work.models import Setting, Logs

CHOICES = {
    'Раз в минуту': {'minute': "*/1"},
    'Раз в день': {'day': "*/1"},
    'Раз в неделю': {'week': '*/1'},
    'Раз в месяц': {'month': '*/1'},
}


def help_mixin(data: Setting, command, status) -> None:
    Logs.objects.create(
        title=f'{command}: {data.mailing_name}',
        date_last=now(),
        status=f'{status}',
        answer='good',
        settings=data,
    )


class AutoMail:

    def __init__(self, data):
        self.scheduler = BackgroundScheduler()
        self.data: Setting = data
        self.__create_automail()
        self.scheduler.start()

    def __create_automail(self):
        """Создание задания"""
        self.assd = self.scheduler.add_job(
            self.__preparation_sending,
            trigger='cron',
            **(CHOICES.get(self.data.periodicity)),
            start_date=self.data.date_mailing,
        )

        help_mixin(self.data, 'Создана задача', 'Рассылка активирована')

    def __preparation_sending(self):
        """"""
        setting = Setting.objects.get(mailing_name=self.data.mailing_name)
        setting.status = 'Активна'
        setting.save()

        if now() < self.data.date_end_mailing:
            self.mail_to()
        else:
            setting.status = 'Завершена'
            setting.save()
            self.assd.remove()

            help_mixin(self.data, 'Рассылка завершена', 'Good')

    def mail_to(self):
        """Отправка сообщений по адресам"""

        for client in self.data.client_name.all():
            send_mail(
                self.data.message.theme,
                self.data.message.body,
                settings.EMAIL_HOST_USER,
                recipient_list=[client.email],
            )

            help_mixin(self.data, f'Письмо отправлено {client.email}', 'Отправлено')
