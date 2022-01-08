# Generated by Django 2.2.13 on 2022-01-07 10:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20220107_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oder',
            name='customer_phone_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\1?\\d{9,10}$')]),
        ),
    ]