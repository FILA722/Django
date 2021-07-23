from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название ')
    content = forms.CharField(label='Новость ', required=False)
    is_published = forms.BooleanField(label="Опубликовано ", required=False, initial=True)
    category = forms.ModelChoiceField(empty_label="Выберите категорию", queryset=Category.objects.all(), label="Категория ")