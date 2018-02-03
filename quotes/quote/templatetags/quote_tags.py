from ..models import Tag
from django import template
from django.db.models.aggregates import Count

register=template.Library()

@register.simple_tag
def get_most_tags():
    return Tag.objects.annotate(num_quote=Count('quote'))