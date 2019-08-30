from django.shortcuts import render
from django.utils.translation import gettext as _

from .models import Product
from document.views import doc_list

# Create your views here.
def list_fire_door(request):
    frd = Product.objects.filter(product_type='frd')
    dhw = Product.objects.filter(product_type='dhw')
    docs = doc_list('frd')

    return render(request, 'product/frd_list.html', {
        'product_desc': _('frd-desc'),
        'please_click': _('please-click'),
        'frd': frd,
        'dhw': dhw,
        'docs': docs,
    })

def list_fire_damper(request):
    fdc = Product.objects.filter(product_type='fdc')
    docs = doc_list('fdc')

    return render(request, 'product/fdc_list.html', {
        'product_desc': _('fdc-desc'),
        'please_click': _('please-click'),
        'fdc': fdc,
        'docs': docs,
    })

def list_fsd_ul(request):
    fsd_ul = Product.objects.filter(product_type='fsd-ul')
    docs = doc_list('fsd-ul')

    return render(request, 'product/fsd_ul_list.html', {
        'product_desc': _('fsd-ul-desc'),
        'please_click': _('please-click'),
        'fsd_ul': fsd_ul,
        'docs': docs,
    })

def list_other_damper(request):
    ddp = Product.objects.filter(product_type='ddp')
    docs = doc_list('ddp')

    return render(request, 'product/ddp_list.html', {
        'product_desc': _('ddp-desc'),
        'please_click': _('please-click'),
        'ddp': ddp,
        'docs': docs,
    })

def list_duct_silencer(request):
    ds = Product.objects.filter(product_type='ds')
    docs = doc_list('ds')

    return render(request, 'product/ds_list.html', {
        'product_desc': _('ds-desc-1') + "<br><br>" + _('ds-desc-2'),
        'please_click': _('please-click'),
        'ds': ds,
        'docs': docs,
    })

def list_air_outlet(request):
    aol = Product.objects.filter(product_type='aol')
    docs = doc_list('aol')

    return render(request, 'product/aol_list.html', {
        'product_desc': _('aol-desc'),
        'please_click': _('please-click'),
        'aol': aol,
        'docs': docs,
    })
