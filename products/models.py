from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Meals(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    price = models.DecimalField(default = 0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default = 0.00, max_digits=7, decimal_places=2, verbose_name='Скидка')
    image = models.ImageField(upload_to='meals_image', blank=True, null=True, verbose_name='Изображение')
    product_id = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')
    
    class Meta():
        db_table = 'meals'
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount/100, 2)
        return self.price