from django import template
from django.db.models import Sum
from django.core.cache import cache

from news.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('components/list_categories.html')
def show_categories():
    categories = cache.get('categories')
    if not categories:
        categories = Category.objects.annotate(cnt=Sum('news__is_published')).filter(cnt__gt=0)
        cache.set('categories', categories, 60)
    return {"categories": categories}


@register.filter()
def to_int(value):
    return int(value)
