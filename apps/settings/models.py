from django.db import models

# Create your models here.
class Settings(models.Model):
    name_site = models.CharField(
        max_length=244,
        verbose_name="Название сайта"
    )

    logo_site = models.ImageField(
        upload_to='logo_site/',
        verbose_name='Логотип сайта'
    )
    
    description_site = models.TextField(
        verbose_name="Описание сайта"
    )

    def __str__(self):
        return self.name_site

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = " Настройки сайта"
         

class Slide(models.Model):
    slide_image_1 = models.ImageField(
        upload_to='slide_image/',
        verbose_name="Фотография первого слайда"
    )

    slide_image_2 = models.ImageField(
        upload_to='slide_image/',
        verbose_name="Фотография второго слайда"
    )

    
    