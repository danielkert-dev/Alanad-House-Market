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


@register.filter(name='replace_underscores')
def replace_underscores(value):
    return value.replace('_', ' ')

@register.filter
def split_string(value):
    return value.split(',')

@register.filter
def extract_image_links(high_img):
    high_img = high_img.strip('{}')  # Remove curly braces
    image_links = [link.strip('"') for link in high_img.split(',')]  # Remove double quotes
    return image_links