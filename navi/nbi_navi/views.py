from django.shortcuts import render
from django.http import HttpResponse
from .models import News #чтоб достать данные из News


def index(request):
    news = News.objects.all
    data = {'news': news, 'title': 'Список новостей'}
    return render(request, 'nbi_navi/index.html', data)  #request, temple_name, DATA
