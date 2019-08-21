from django.shortcuts import render
from news.views import news_list
from project.views import project_list
from django.conf import settings
from django.utils.translation import get_language
import os

# Create your views here.
def page_home(request, *args, **kwargs):
    news_queryset = news_list(request, 2)
    project_queryset = project_list(request, 3)

    LANG = get_language()
    path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'carousel', LANG)
    carousel_images = os.listdir(path)
    for i, img in enumerate(carousel_images):
        carousel_images[i] = 'images/carousel/'+ LANG + '/' + img

    return render(request, 'page/page_home.html' , {
        'news_queryset': news_queryset,
        'project_queryset': project_queryset,
        'carousel_images': carousel_images,
    })

def page_about(request, *args, **kwargs):
    path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'factory')
    factory_images = os.listdir(path)
    for i, img in enumerate(factory_images):
        factory_images[i] = 'images/factory/' + img

    return render(request, 'page/page_about.html' , {
        'factory_images': factory_images,
        }
    )

def page_contact(request, *args, **kwargs):
    return render(request, 'page/page_contact.html')

def page_career(request, *args, **kwargs):
    return render(request, 'page/page_career.html')
