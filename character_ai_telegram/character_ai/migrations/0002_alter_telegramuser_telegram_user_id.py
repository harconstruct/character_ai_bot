# Generated by Django 4.2.2 on 2023-07-05 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character_ai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='telegram_user_id',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
