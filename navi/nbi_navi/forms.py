from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError

#Модель не связанная с формой
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150,
#                             label='Название ',
#                             widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(label='Новость ',
#                               required=False,
#                               widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
#     is_published = forms.BooleanField(label="Опубликовано ", required=False, initial=True)
#     category = forms.ModelChoiceField(empty_label="Выберите категорию",
#                                       queryset=Category.objects.all(),
#                                       label="Категория ",
#                                       widget=forms.Select(attrs={"class": "form-control"}))

class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].empty_label = "Выберите категорию"

    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", 'rows': 5}),
            'category': forms.Select(attrs={"class": "form-control"})
        }
    #валидатор для поля title
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('название не должно начинаться с цифры')
        return title