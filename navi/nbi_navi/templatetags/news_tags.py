from django import template
from nbi_navi.models import Category

register = template.Library()  #регистрация TemplateTag

@register.simple_tag()
def get_categories():
    return Category.objects.all()