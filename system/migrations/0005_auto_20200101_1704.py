# Generated by Django 2.1.7 on 2020-01-01 11:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_auto_20200101_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='phone_no',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be 10 Digit.', regex='^\\d{10}$')]),
        ),
    ]
