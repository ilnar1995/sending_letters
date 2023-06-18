# Generated by Django 4.1 on 2023-06-18 16:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Tag')),
                ('operator_code', models.CharField(editable=False, max_length=3, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Operator code')),
                ('phone_number', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Номер телефона клиента в формате 7XXXXXXXXXX (X-цифра от 0 до 9)', regex='^7\\d{10}$')], verbose_name='Phone number')),
            ],
            options={
                'db_table': 'app_sending_letters_client',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('filter_mobile_operator_code', models.CharField(blank=True, max_length=3, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Search by mobile operator code')),
                ('filter_tag', models.CharField(blank=True, max_length=50, verbose_name='Tag')),
            ],
            options={
                'db_table': 'app_sending_letters_campaign',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Tag')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='sending_letters.mailing')),
            ],
            options={
                'db_table': 'app_sending_letters_message',
                'ordering': ['id'],
            },
        ),
    ]
