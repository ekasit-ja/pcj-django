from django.shortcuts import render
from django.utils.translation import gettext as _

from .models import Product
from document.views import doc_list

# Create your views here.
def list_fire_door(request):
    dhw = Product.objects.filter(product_type='dhw')
    docs = doc_list('frd')

    return render(request, 'product/frd_list.html', {
        'product_desc': _('frd-desc'),
        'please_click': _('please-click'),
        'dhw': dhw,
        'docs': docs,
    })

def list_fire_damper(request):
    pass

def list_fsd_ul(request):
    pass

def list_other_damper(request):
    pass

def list_duct_silencer(request):
    pass

def list_air_outlet(request):
    pass
