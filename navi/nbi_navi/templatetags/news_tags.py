from django import template
from nbi_navi.models import Category

register = template.Library()  #регистрация TemplateTag

@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('nbi_navi/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}