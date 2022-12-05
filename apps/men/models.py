from django.db import models

# Create your models here.
class Men(models.Model):
    product_image_1 = models.ImageField(upload_to='Product_image_men',verbose_name='Первая Фотография  продукт', blank= True,null=True)
    product_image_2 = models.ImageField(upload_to='Product_image_men',verbose_name='Вторая Фотография продукт', blank= True,null=True)
    product_image_3 = models.ImageField(upload_to='Product_image_men',verbose_name='Третья Фотография продукт', blank= True,null=True)
    product_image_4 = models.ImageField(upload_to='Product_image_men',verbose_name='Четвертая Фотография продукт', blank= True,null=True)

    name = models.CharField(max_length=255,verbose_name='Название продукта')
    price = models.CharField(max_length=244,verbose_name='Цена продукта!')
    desc = models.TextField(verbose_name='Описание продукта!')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мужская одежда"
        verbose_name_plural = "Мужская одежда"