from django.db import models

from user.models import User

class Reservation(models.Model):

    user = models.ForeignKey(to=User, default=None, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Пользователь")
    phone = models.CharField(max_length=100, verbose_name="Номер телефона")
    quantity = models.IntegerField(default=0, verbose_name="Количество людей")
    date = models.CharField(max_length=100, verbose_name="Дата заказа")
    time = models.CharField(max_length=100, verbose_name="Время заказа")
    comment = models.TextField(null=True, blank=True, verbose_name="Дополнительная информация")
    created_timestemp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания запроса на резервацию")
    accepted = models.BooleanField(default=False, verbose_name="Обработано")
    

    class Meta:
        db_table = "reservation"
        verbose_name = "Зарезервированный стол"
        verbose_name_plural = "Зарезервированные столы"

    
        



