# Generated by Django 2.0.7 on 2018-08-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usext', '0002_auto_20180807_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextends',
            name='vip',
            field=models.DateTimeField(help_text='Дата по которую пользователь имеет ВИП-статус'),
        ),
    ]
