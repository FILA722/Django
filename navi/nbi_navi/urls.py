from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='home'), #для функции во views
    path('', HomeNews.as_view(), name='home'), #для класса во views

    # path('category/<int:category_id>/', get_category, name='category'), # category/{1,2,3,4...} принимает id категории
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title': 'title'}), name='category'),

    path('navi', navi, name='navi'),

    # path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:news_id>/', ViewNews.as_view(), name='view_news'),

    path('news/add-news/', add_news, name='add_news'),
]