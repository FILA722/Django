from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News, Category #чтоб достать данные из News
from .forms import NewsForm
from django.views.generic import ListView

class HomeNews(ListView):
    model = News
    template_name = 'nbi_navi/index.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная'} #так не рекомендуется выводить титул страницы

    #Название страницы:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
    #публиковать новости только с выбранным полем "Опубликовать"
    def get_queryset(self):
        return News.objects.filter(is_published=True)


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
        form = NewsForm(request.POST) #забрать данные с формы
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data) # Для модели не связанной с формой
            news = form.save() # Для модели связанной с формой
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'nbi_navi/add_news.html', {'form': form})
