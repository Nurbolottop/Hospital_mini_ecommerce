from django.db import models

# Create your models here.
class Banner(models.Model):
    image_1 = models.ImageField(upload_to='banner_image', verbose_name='Первая фотография банера!')
    image_2 = models.ImageField(upload_to='banner_image', verbose_name='Вторая фотография банера!')
    image_3 = models.ImageField(upload_to='banner_image', verbose_name='Третья фотография банера!')
    image_4 = models.ImageField(upload_to='banner_image', verbose_name='Четвертая фотография банера!')

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннер"