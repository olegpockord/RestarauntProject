
from django import template

from products.models import Categories, Meals


register = template.Library()



@register.simple_tag()
def tag_products():
    return Meals.objects.all()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

