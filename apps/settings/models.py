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

class Men(models.Model):
    product_image_1 = models.ImageField(upload_to='Product_image',verbose_name='Фотография продукт', blank= True,null=True)
    product_image_2 = models.ImageField(upload_to='Product_image',verbose_name='Фотография продукт', blank= True,null=True)
    product_image_3 = models.ImageField(upload_to='Product_image',verbose_name='Фотография продукт', blank= True,null=True)
    product_image_4 = models.ImageField(upload_to='Product_image',verbose_name='Фотография продукт', blank= True,null=True)

    name = models.CharField(max_length=255,verbose_name='Название продукта')
    price = models.CharField(max_length=244,verbose_name='Цена продукта!')
    desc = models.TextField(verbose_name='Описание продукта!')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мужская одежда"
        verbose_name_plural = "Мужская одежда"

class Women(models.Model):
    product_image_1 = models.ImageField(upload_to='Product_image',verbose_name='Фотография продукт', blank= True,null=True)
    product_image_2 = models.ImageField(upload_to='Product_image',verbose_name='Фотография продукт', blank= True,null=True)
    product_image_3 = models.ImageField(upload_to='Product_image',verbose_name='Фотография продукт', blank= True,null=True)
    product_image_4 = models.ImageField(upload_to='Product_image',verbose_name='Фотография продукт', blank= True,null=True)

    name = models.CharField(max_length=255,verbose_name='Название продукта')
    price = models.CharField(max_length=244,verbose_name='Цена продукта!')
    desc = models.TextField(verbose_name='Описание продукта!')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Женская одежда"
        verbose_name_plural = "Женская одежда"

class Banner(models.Model):
    image_1 = models.ImageField(upload_to='banner_image', verbose_name='Первая фотография банера!')
    image_2 = models.ImageField(upload_to='banner_image', verbose_name='Вторая фотография банера!')
    image_3 = models.ImageField(upload_to='banner_image', verbose_name='Третья фотография банера!')
    image_4 = models.ImageField(upload_to='banner_image', verbose_name='Четвертая фотография банера!')

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннер"
