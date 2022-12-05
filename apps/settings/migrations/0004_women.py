# Generated by Django 4.1.1 on 2022-12-05 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_men'),
    ]

    operations = [
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image_1', models.ImageField(blank=True, null=True, upload_to='Product_image', verbose_name='Фотография продукт')),
                ('product_image_2', models.ImageField(blank=True, null=True, upload_to='Product_image', verbose_name='Фотография продукт')),
                ('product_image_3', models.ImageField(blank=True, null=True, upload_to='Product_image', verbose_name='Фотография продукт')),
                ('product_image_4', models.ImageField(blank=True, null=True, upload_to='Product_image', verbose_name='Фотография продукт')),
                ('name', models.CharField(max_length=255, verbose_name='Название продукта')),
                ('price', models.CharField(max_length=244, verbose_name='Цена продукта!')),
                ('desc', models.TextField(verbose_name='Описание продукта!')),
            ],
            options={
                'verbose_name': 'Женская одежда',
                'verbose_name_plural': 'Женская одежда',
            },
        ),
    ]
