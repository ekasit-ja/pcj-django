from django.urls import path
from .views import (
    # ArticleCreateView,
    # ArticleDeleteView,
    # ArticleDetailView,
    FinanceListView,
    # ArticleUpdateView,
)

app_name = 'finance'
urlpatterns = [
    path('', FinanceListView.as_view(), name='finance-list'),
    # path('create/', ArticleCreateView.as_view(), name='article-create'),
    # path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    # path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]
