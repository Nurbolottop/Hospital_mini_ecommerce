from django.db import models

# Create your models here.
class Slide(models.Model):

    slide_image_1 = models.ImageField(
        upload_to='slide_image/',
        verbose_name="Фотография первого слайда"
    )

    name_slide_1 = models.CharField(
        max_length=244,
        verbose_name="Название первого слайда"
    )

    desc_slide_1 = models.TextField(
        verbose_name="Описание первого слайда"
    )

    slide_image_2 = models.ImageField(
        upload_to='slide_image/',
        verbose_name="Фотография второго слайда"
    )

    name_slide_2 = models.CharField(
        max_length=244,
        verbose_name="Название второго слайда"
    )

    desc_slide_2 = models.TextField(
        verbose_name="Описание первого слайда"
    )

    def __str__(self):
        return self.name_slide_1

    class Meta:
        verbose_name = "Слайды"
        verbose_name_plural = "Слайды"