from django.urls import path
from .views import (
    # ArticleCreateView,
    # ArticleDeleteView,
    # ArticleDetailView,
    ProductListView,
    # ArticleUpdateView,
)

app_name = 'product'
urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    # path('create/', ArticleCreateView.as_view(), name='article-create'),
    # path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    # path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]
