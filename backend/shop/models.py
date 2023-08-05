from django.db import models
from django.utils.translation import gettext_lazy as _


class Group(models.Model):
    """
     Модель группы товаров
    """
    name = models.CharField(max_length=255, verbose_name='Наименование группы')
    slug  = models.SlugField(max_length=50, unique=True, verbose_name='Slug')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Группа товара'
        verbose_name_plural='Группа товаров'


class Manufacturer(models.Model):
    """
    Производтель товара
    """
    name = models.CharField(max_length=255, verbose_name='Наименование производителя')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Производтель товара'
        verbose_name_plural='Производтель товаров'

    
class Product(models.Model):
    """ 
     Модель товара
    """
    class Status(models.TextChoices):
     # Actual value ↓      # ↓ Displayed on Django Admin  
        IN_STOCK   = 'In_stock', _('Есть в наличии')
        ABSENT   = 'Absent', _('Временно отсутсвует')
        ON_MY_WAY  = 'On_my_way', _('В пути')

    title       = models.CharField('Наименование товара', max_length=255)
    description = models.TextField('Описание', max_length=5000)
    price       = models.IntegerField('Цена', default=0)
    vendor_code = models.CharField('Артикул', max_length=255)
    pub_date    = models.DateTimeField('Дата публикации', auto_now_add=True)
    status      = models.CharField('Статус', max_length=10, choices=Status.choices, default='IN_STOCK',)
    group       = models.ForeignKey(Group, on_delete=models.CASCADE, 
                                    related_name='products', 
                                    verbose_name='Группа', 
                                    help_text='Выберете группу')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, 
                                     related_name='products', 
                                     verbose_name='Производитель', 
                                     help_text='Выберете производителя')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Image(models.Model):
    """
     Картинка товара
    """
    def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/product_<id>/<filename>
        return "images/product_{0}/{1}".format(instance.product.id, filename)
    
    file    = models.ImageField(upload_to=user_directory_path)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')


    class Meta:
        verbose_name = 'Картинка товара'
        verbose_name_plural = 'Картинки товаров'