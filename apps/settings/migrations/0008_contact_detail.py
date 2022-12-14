# Generated by Django 4.1.1 on 2022-12-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_alter_contacts_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
    ]
