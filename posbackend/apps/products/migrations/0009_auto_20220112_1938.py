# Generated by Django 3.0.5 on 2022-01-12 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0002_auto_20220112_1108'),
        ('category', '0003_auto_20220112_1924'),
        ('brands', '0001_initial'),
        ('products', '0008_auto_20220112_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='attribute_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.Attribute'),
        ),
        migrations.AlterField(
            model_name='products',
            name='brand_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.Brands'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category'),
        ),
    ]
