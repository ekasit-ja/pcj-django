from django.shortcuts import render
from news.views import news_list
from project.views import project_list


# Create your views here.
def page_home(request, *args, **kwargs):
    news_queryset = news_list(request, 2)
    project_queryset = project_list(request, 3)

    return render(request, 'page/page_home.html' , {
        'news_queryset': news_queryset,
        'project_queryset': project_queryset,
    })

def page_about(request, *args, **kwargs):
    return render(request, 'page/page_about.html')
