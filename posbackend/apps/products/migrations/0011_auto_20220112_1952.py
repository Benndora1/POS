# Generated by Django 3.0.5 on 2022-01-12 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0002_auto_20220112_1108'),
        ('products', '0010_auto_20220112_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='attribute_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='attribute.Attribute'),
        ),
    ]
