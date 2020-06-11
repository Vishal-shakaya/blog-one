from urllib.parse import urlparse
from django import template
register = template.Library()

@register.filter
def urlshr(value):
	return urlparse(value) 