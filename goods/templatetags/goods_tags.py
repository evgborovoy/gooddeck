from goods.models import Categories
from django import template

register = template.Library()
@register.simple_tag()
def teg_categories():
    return Categories.objects.all()
