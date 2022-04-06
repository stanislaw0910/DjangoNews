from django import template
from django.db import models
from django.urls import reverse
from django.utils.html import format_html_join

from ..models import Tags


register = template.Library()


@register.simple_tag()
def tagcloud():
    url = reverse('news')
    tags = Tags.objects.all()
    tags = tags.annotate(count=models.Count('news'))
    tags = tags.order_by('name').values_list('name', 'count')
    fmt = '<a href="%s?tag={0}">{0} ({1})</a>' % url
    return format_html_join(', ', fmt, tags)
