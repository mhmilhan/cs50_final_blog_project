from django import template

register = template.Library()

@register.filter(name='add_attrs')
def add_attrs(field, args):
    css_class, placeholder = args.split(',')
    return field.as_widget(attrs={"class": css_class, "placeholder": placeholder})