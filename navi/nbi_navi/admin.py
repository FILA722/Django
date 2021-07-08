from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    """
    Этот класс отвечает за отображение нужных полей из БД в админке
    """
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
# Register your models here.
admin.site.register(News, NewsAdmin) #To Registry model News and NewsAdmin