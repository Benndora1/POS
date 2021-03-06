# Generated by Django 2.2.13 on 2022-01-07 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_oder_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oder',
            name='customer_address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='oder',
            name='customer_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='oder',
            name='customer_phone_number',
            field=models.IntegerField(blank=True, default=10),
        ),
    ]
