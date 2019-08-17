from django.shortcuts import render
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)

from .models import News, NewsImage

# Create your views here.
class NewsListView(ListView):
    template_name = 'news/news_list.html'
    queryset = News.objects.all()

def news_list(request, qty):
    news = News.objects.all()[:qty]
    for new in news:
        new.firstNewsImage = NewsImage.objects.filter(news=new.id).first()

    return news
