from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
path('', views.CreateOrderView.as_view(), name='create-order'),
    
]