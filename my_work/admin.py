from django.contrib import admin

from my_work.models import Client, Setting, Messages, Logs


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'comment', 'is_active')


@admin.register(Setting)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('mailing_name', 'message', 'date_mailing', 'date_end_mailing', 'is_active', 'periodicity')
    filter_horizontal = ('user_name',)


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('theme', 'body', 'is_active')


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_last', 'status', 'answer')
   # list_filter = ('settings_mailing_name',)
