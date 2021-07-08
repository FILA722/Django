from django.contrib import admin
from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    """
    Этот класс отвечает за отображение нужных полей из БД в админке
    """
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',) #чтоб менять из админки
    list_filter = ('is_published', 'category') #добавить в админку поле с функцией фильтрации

class CategoryAdmin(admin.ModelAdmin):
    """
    Этот класс отвечает за отображение нужных полей из БД в админке
    """
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

# Register your models here.
admin.site.register(News, NewsAdmin) #To Registry model News and NewsAdmin
admin.site.register(Category, CategoryAdmin)