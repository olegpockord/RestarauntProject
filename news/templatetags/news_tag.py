from django import template

from news.models import Event, NewsCategory

register = template.Library()

@register.simple_tag()
def tag_news():
    return Event.objects.all()

@register.simple_tag()
def tag_news_category():
    return NewsCategory.objects.all()