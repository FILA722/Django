from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category #чтоб достать данные из News


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    data = {'news': news, 'title': 'Список новостей', 'categories': categories}
    return render(request, 'nbi_navi/index.html', data)  #request, temple_name, DATA

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'nbi_navi/category.html', {'news': news, 'categories': categories, 'category': category})

def navi(request):
    active_companies = [['pepsi', 'coke'], ['mercedes', 'WV']]
    data = {'title': 'NBI Navigator'}
    return render(request, 'nbi_navi/navi.html', data)