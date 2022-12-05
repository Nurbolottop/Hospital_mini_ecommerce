from django.db import models

# Create your models here.
class Contacts(models.Model):
    phone = models.CharField(max_length=255,verbose_name='Телефонный номер ')
    email = models.EmailField(verbose_name='Почта')
    address = models.CharField(max_length=255,verbose_name='Адрес')
    facebook = models.URLField(verbose_name="Facebook", blank=True ,null= True)
    instagram = models.URLField(verbose_name="Instagram", blank=True ,null= True)
    telegram = models.URLField(verbose_name="Telegram", blank=True ,null= True)
    whatsapp = models.URLField(verbose_name="Whatsapp", blank=True ,null= True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

class Contact_detail(models.Model):
    name = models.CharField(max_length=244,verbose_name="Имя")
    email = models.EmailField(verbose_name='Почта')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"