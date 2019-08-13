from django.shortcuts import render
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)

from .models import News

# Create your views here.
class NewsListView(ListView):
    template_name = 'news/news_list.html'
    queryset = News.objects.all()
