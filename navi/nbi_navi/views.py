from django.shortcuts import render
from django.http import HttpResponse
from .models import News #чтоб достать данные из News


def index(request):
    news = News.objects.all()
    res = '<h1>Список новостей</h1>\n'
    for new in news:
        res += f'<div>\n<p>{new.title}</p>\n<p>{new.content}</p>\n</div>\n<hr>'
    return HttpResponse(res)

def test(request):
    return HttpResponse('<h1>Тестовая страница</h1>')