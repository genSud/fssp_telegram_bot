# Generated by Django 2.0.1 on 2018-03-24 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valuename', models.CharField(blank='False', max_length=1000, null='False', verbose_name='Имя')),
                ('value', models.CharField(blank='False', max_length=1000, null='False', verbose_name='Значение')),
            ],
        ),
    ]