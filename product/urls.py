from django.urls import path
from .views import (
    list_fire_door,
    list_fire_damper,
    list_fsd_ul,
    list_other_damper,
    list_duct_silencer,
    list_air_outlet,
)

app_name = 'product'
urlpatterns = [
    path('fire-steel-door', list_fire_door, name='product-frd'),
    path('fire-damper', list_fire_damper, name='product-fdc'),
    # path('fsd-ul', list_fsd_ul, name='product-fsd-ul'),
    path('duct-damper', list_other_damper, name='product-ddp'),
    path('duct-silencer', list_duct_silencer, name='product-ds'),
    path('air-outlet', list_air_outlet, name='product-aol'),
]
