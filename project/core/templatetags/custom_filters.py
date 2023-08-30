import re
from django import template

register = template.Library()


@register.filter
def remove_text(value, text_to_remove):
    """
    Custom template filter to remove specified text from the input string.
    Usage: {{ house.description|remove_text:"Visa hela beskrivningen" }}
    """
    pattern = re.escape(text_to_remove)
    value = re.sub(pattern, '', value)
    return value

@register.filter
def slice_range(value, start):
    return value[start:start + 10]

@register.simple_tag
def get_paginated_url(request, page_number):
    query_params = request.GET.copy()
    query_params['page'] = page_number
    return '?' + query_params.urlencode()