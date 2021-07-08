from django.shortcuts import render
from django.http import HttpResponse
from .models import News #чтоб достать данные из News


def index(request):
    news = News.objects.all()
    return render(request, 'nbi_navi/index.html', {'news': news, 'title': 'Список новостей'})  #request, temple_name, DATA
