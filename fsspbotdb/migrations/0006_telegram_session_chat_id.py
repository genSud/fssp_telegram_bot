# Generated by Django 2.0.1 on 2018-03-31 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsspbotdb', '0005_auto_20180328_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegram_session',
            name='chat_id',
            field=models.BigIntegerField(null='False'),
        ),
    ]
