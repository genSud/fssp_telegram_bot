# Generated by Django 2.0.1 on 2018-05-11 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsspbotdb', '0011_auto_20180511_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.DateTimeField(null='True'),
        ),
        migrations.AlterField(
            model_name='job',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
