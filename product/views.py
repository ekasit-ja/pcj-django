from django.shortcuts import render
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)

from .models import Product

# Create your views here.
class ProductListView(ListView):
    template_name = 'product/product_list.html'
    queryset = Product.objects.all()
