from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News, Category #чтоб достать данные из News
from .forms import NewsForm

def index(request):
    news = News.objects.all()
    data = {'news': news, 'title': 'Список новостей'}
    return render(request, 'nbi_navi/index.html', data)  #request, temple_name, DATA

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'nbi_navi/category.html', {'news': news, 'category': category})

def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'nbi_navi/view_news.html', {'news_item': news_item})

def navi(request):
    data = {'title': 'NBI Navigator'}
    return render(request, 'nbi_navi/navi.html', data)

def add_news(request):
    if request.method == "POST":
        pass
    else:
        form = NewsForm()
    return render(request, 'nbi_navi/add_news.html', {'form': form})
