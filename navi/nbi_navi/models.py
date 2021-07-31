from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', related_name='get_news')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'news_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        """
        Этот класс отвечает за отображение полей на странице
        """
        verbose_name = 'Новость' #Единичное склонение
        verbose_name_plural = 'Новости' #Множественное склонение
        ordering = ['-created_at', 'title'] #Порядок отображения

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        """
        Этот класс отвечает за отображение полей на странице
        """
        verbose_name = 'Категория' #Единичное склонение
        verbose_name_plural = 'Категории' #Множественное склонение
        ordering = ['title'] #Порядок отображения