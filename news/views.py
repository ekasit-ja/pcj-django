from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import News, NewsImage

# Create your views here.
class NewsListView(ListView):
    template_name = 'news/news_list.html'

    def get_queryset(self):
        queryset = News.objects.all()
        for new in queryset:
            new.firstNewsImage = NewsImage.objects.filter(news=new.id).first()

        return queryset

class NewsDetailView(DetailView):
    template_name = 'news/news_detail.html'

    def get_object(self):
        news_id = self.kwargs.get('id')
        return get_object_or_404(News, id=news_id)

def news_list(request, qty):
    news = News.objects.all()[:qty]
    for new in news:
        new.firstNewsImage = NewsImage.objects.filter(news=new.id).first()

    return news
