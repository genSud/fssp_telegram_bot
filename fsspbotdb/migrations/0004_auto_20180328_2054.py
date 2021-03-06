# Generated by Django 2.0.1 on 2018-03-28 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsspbotdb', '0003_setting_valuename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cookie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(null='False')),
                ('value_name', models.CharField(blank='False', max_length=1000, null='False', verbose_name='Название')),
                ('name', models.CharField(blank='False', max_length=1000, null='False', verbose_name='Значение')),
            ],
        ),
        migrations.CreateModel(
            name='Telegram_session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_id', models.BigIntegerField(null='False')),
                ('message_id', models.BigIntegerField(null='False')),
                ('message_date', models.DateTimeField(auto_now=True)),
                ('user_id', models.BigIntegerField(null='False')),
                ('status', models.BooleanField(verbose_name='Статус')),
            ],
        ),
        migrations.AlterField(
            model_name='setting',
            name='valuename',
            field=models.CharField(choices=[('TELETOKEN', 'Telegram Token'), ('FSSPTOKEN', 'FSSP Token')], default='TELETOKEN', max_length=100),
        ),
    ]
