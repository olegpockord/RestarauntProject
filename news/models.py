from django.db import models

class NewsCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'    

    def __str__(self):
        return self.name


class Event(models.Model):

    name = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='news_image', blank=True, null=True, verbose_name='Изображение')
    content = models.TextField(unique=True, null=True, verbose_name='Содержимое')
    event = models.ForeignKey(to=NewsCategory, on_delete=models.CASCADE)
    time = models.CharField(max_length=50, blank=True, null=True, verbose_name='Время')

    class Meta:
        db_table = 'events'
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.name
