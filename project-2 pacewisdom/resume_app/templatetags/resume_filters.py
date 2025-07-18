from django import template
register = template.Library()
@register.filter
def split_lines(value):
    if value:
        lines = [line.strip() for line in value.split('\n') if line.strip()]
        return lines
    return []