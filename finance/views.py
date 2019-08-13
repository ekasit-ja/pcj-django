from django.shortcuts import render
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)

from .models import Finance

# Create your views here.
class FinanceListView(ListView):
    template_name = 'finance/finance_list.html'
    queryset = Finance.objects.all()
