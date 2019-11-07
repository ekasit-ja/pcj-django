from django.urls import path
from .views import (
    NewsListView,
    news_detail,
)

app_name = 'news'
urlpatterns = [
    path('', NewsListView.as_view(), name='news-list'),
    path('<int:id>/', news_detail, name='news-detail'),
]
