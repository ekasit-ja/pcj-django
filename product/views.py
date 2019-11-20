from django.shortcuts import render
from django.utils.translation import gettext as _
from django.template.defaultfilters import striptags, truncatechars
from django.templatetags.static import static

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
        'products': frd,
        'dhw': dhw,
        'docs': docs,
        'meta_title': _('meta-title-frd')+" | "+_('pcj-industries-short'),
        'meta_desc': _('meta-desc-frd'),
        'meta_kw': _('meta-kw-frd'),
        'meta_img': request.build_absolute_uri(static('images/fire_doors.jpg')),
        'meta_robots': 'index, nofollow',
    })

def list_fire_damper(request):
    fdc = Product.objects.filter(product_type='fdc')
    docs = doc_list('fdc')

    return render(request, 'product/fdc_list.html', {
        'product_desc': _('fdc-desc'),
        'please_click': _('please-click'),
        'products': fdc,
        'docs': docs,
        'meta_title': _('meta-title-fdc')+" | "+_('pcj-industries-short'),
        'meta_desc': _('meta-desc-fdc'),
        'meta_kw': _('meta-kw-fdc'),
        'meta_img': request.build_absolute_uri(static('images/fire_dampers.jpg')),
        'meta_robots': 'index, nofollow',
    })

def list_fsd_ul(request):
    fsd_ul = Product.objects.filter(product_type='fsd-ul')
    docs = doc_list('fsd-ul')

    return render(request, 'product/fsd_ul_list.html', {
        'product_desc': _('fsd-ul-desc'),
        'please_click': _('please-click'),
        'products': fsd_ul,
        'docs': docs,
        'meta_title': _('meta-title-fsd-ul')+" | "+_('pcj-industries-short'),
        'meta_desc': _('meta-desc-fsd-ul'),
        'meta_kw': _('meta-kw-fsd-ul'),
        'meta_img': request.build_absolute_uri(static('images/fsd_ul.jpg')),
        'meta_robots': 'index, nofollow',
    })

def list_other_damper(request):
    ddp = Product.objects.filter(product_type='ddp')
    docs = doc_list('ddp')

    return render(request, 'product/ddp_list.html', {
        'product_desc': _('ddp-desc'),
        'please_click': _('please-click'),
        'products': ddp,
        'docs': docs,
        'meta_title': _('meta-title-ddp')+" | "+_('pcj-industries-short'),
        'meta_desc': _('meta-desc-ddp'),
        'meta_kw': _('meta-kw-ddp'),
        'meta_img': request.build_absolute_uri(static('images/duct_dampers.jpg')),
        'meta_robots': 'index, nofollow',
    })

def list_duct_silencer(request):
    ds = Product.objects.filter(product_type='ds')
    docs = doc_list('ds')

    return render(request, 'product/ds_list.html', {
        'product_desc': _('ds-desc-1') + "<br><br>" + _('ds-desc-2'),
        'please_click': _('please-click'),
        'products': ds,
        'docs': docs,
        'meta_title': _('meta-title-ds')+" | "+_('pcj-industries-short'),
        'meta_desc': _('meta-desc-ds'),
        'meta_kw': _('meta-kw-ds'),
        'meta_img': request.build_absolute_uri(static('images/duct_silencers.jpg')),
        'meta_robots': 'index, nofollow',
    })

def list_air_outlet(request):
    aol = Product.objects.filter(product_type='aol')
    docs = doc_list('aol')

    return render(request, 'product/aol_list.html', {
        'product_desc': _('aol-desc'),
        'please_click': _('please-click'),
        'products': aol,
        'docs': docs,
        'meta_title': _('meta-title-aol')+" | "+_('pcj-industries-short'),
        'meta_desc': _('meta-desc-aol'),
        'meta_kw': _('meta-kw-aol'),
        'meta_img': request.build_absolute_uri(static('images/air_outlets.jpg')),
        'meta_robots': 'index, nofollow',
    })
