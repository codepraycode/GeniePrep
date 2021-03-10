from django import template

register = template.Library()


@register.filter
def percentage(value):
    return format(float(value), ".2%")


@register.filter
def percentToNum(value):
    return round(float(value) * 100, 1)


register.filter('percent', percentage)
register.filter('toWhole', percentToNum)
