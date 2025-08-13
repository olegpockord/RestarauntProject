from django.urls import path

from news import views



app_name = 'news'

urlpatterns = [
    path('', views.NewsPageView.as_view(), name='news_page'),
    path('event/<slug:news_slug>', views.NewsInfoView.as_view(), name='news_info'),
]