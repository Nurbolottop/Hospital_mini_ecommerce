from django.db import models

# Create your models here.
class Testimonials(models.Model):
    image = models.ImageField(upload_to="testimnials_image/", verbose_name='Отзывы')
    name = models.CharField(max_length=245,verbose_name="Имя")
    descriptions = models.TextField(verbose_name='Отзыв')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural =  "Отзывы"