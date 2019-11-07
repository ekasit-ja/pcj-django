from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.utils.translation import gettext as _
from django.template.defaultfilters import striptags, truncatechars

from .models import News

# Create your views here.
class NewsListView(ListView):
    template_name = 'news/news_list.html'
    context_object_name = 'news_queryset'

    def get_queryset(self):
        queryset = News.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta_title'] = _('news').capitalize()
        context['meta_robots'] = 'noindex, follow'
        return context

def news_detail(request, id):
    news = get_object_or_404(News, id=id)

    # Facebook comments are embedded in URI. We have [/en, /th] (called i18n pattern) to
    # separate each language of all pages. However, we want comments of all languages to
    # stay together. Therefore, we have to remove i18n pattern from the URI.
    locator = request.get_full_path()
    fb_href = request.build_absolute_uri(locator[3:])

    return render(request, 'news/news_detail.html', {
        'news': news,
        'meta_title': truncatechars(news.title, 100),
        'meta_desc': truncatechars(striptags(news.content), 200),
        'meta_img': request.build_absolute_uri(news.image.url),
        'meta_robots': 'index, nofollow',
        'data_href': fb_href,
    })

def news_list(request, qty):
    news = News.objects.all()[:qty]
    return news
