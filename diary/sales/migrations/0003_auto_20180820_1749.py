# Generated by Django 2.0.7 on 2018-08-20 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20180820_1707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='product',
            name='month_cost',
            field=models.FloatField(default=0.0),
        ),
    ]
