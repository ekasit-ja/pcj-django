from django.urls import path
from .views import (
    finance_view,
)

app_name = 'finance'
urlpatterns = [
    path('', finance_view, name='finance-view'),
]
