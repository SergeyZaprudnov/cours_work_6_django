# Generated by Django 4.2.3 on 2023-07-19 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_work', '0003_alter_client_options_alter_setting_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='title',
            field=models.CharField(default='<function now at 0x7ff6e095e840>', max_length=100, verbose_name='Название'),
        ),
    ]
