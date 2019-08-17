from django.urls import reverse
from django.utils.translation import get_language


CONSTANTS = {
    'product_choices': [
        ('frd', 'Fire Doors'),
        ('fdc', 'Fire Dampers'),
        ('ddp', 'Duct Dampers'),
        ('ds', 'Duct Silencers'),
        ('aol', 'Air Outlets'),
        ('dhw', 'Door Hardware'),
    ],

    'document_choices': [
        ('catg', 'Catalog'),
        ('inst', 'Installation'),
        ('cert', 'Certificate'),
    ],
}

def default_context(request):
    return {
        'navbar_items': [
            ('about', reverse('page:page-about')),
            ('products', reverse('page:page-home')),
            ('projects', reverse('page:page-home')),
            ('news', reverse('page:page-home')),
            ('contact', reverse('page:page-home')),
            ('career', reverse('page:page-home')),
            ('en', '/en' + request.get_full_path()[3:], 'assets/images/flag_en.png'),
            ('th', '/th' + request.get_full_path()[3:], 'assets/images/flag_th.png'),
        ],
        'navbar_dropdown_items': [
            ('frd-&-non-frd', reverse('page:page-home'), 'assets/images/fire_doors.jpg'),
            ('fdc', reverse('page:page-home'), 'assets/images/fire_dampers.jpg'),
            ('fsd-ul', reverse('page:page-home'), 'assets/images/fsd_ul.jpg'),
            ('ddp', reverse('page:page-home'), 'assets/images/duct_dampers.jpg'),
            ('ds', reverse('page:page-home'), 'assets/images/duct_silencers.jpg'),
            ('aol', reverse('page:page-home'), 'assets/images/air_outlets.jpg'),
        ],
        'LANG': get_language(),
    }
