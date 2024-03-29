# Generated by Django 4.1 on 2023-06-18 16:11
import csv

from django.db import migrations
from django_project.settings import BASE_DIR


def load_csv(apps):
    # запись из CSV файла в БД локации
    Client = apps.get_model('sending_letters', 'Client')
    print('')
    print('Подождите идет запись из CSV файла в БД')
    fhand = open(str(BASE_DIR) + '/sending_letters/default_client.csv')
    reader = csv.reader(fhand)
    count = 0
    for row in reader:
        Client.objects.create(id=row[0], tag=row[1], operator_code=row[2], phone_number=row[3])
        count += 1


def add_default(apps, schema_editor):
    # Запись в БД дефолтных данных
    # pass
    load_csv(apps)


class Migration(migrations.Migration):

    dependencies = [
        ('sending_letters', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default),
    ]
