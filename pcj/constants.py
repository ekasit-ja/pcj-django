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
            ('Fire Steel Doors & Non-Fire Steel Doors', reverse('page:page-home'), 'assets/images/fire_doors.jpg'),
            ('Fire Dampers', reverse('page:page-home'), 'assets/images/fire_dampers.jpg'),
            ('Combination of Fire & Smoke Dampers', reverse('page:page-home'), 'assets/images/fsd_ul.jpg'),
            ('Other Dampers', reverse('page:page-home'), 'assets/images/duct_dampers.jpg'),
            ('Duct Silencers & Acoustic Louvers', reverse('page:page-home'), 'assets/images/duct_silencers.jpg'),
            ('Air Outlets', reverse('page:page-home'), 'assets/images/air_outlets.jpg'),
        ],
        'LANG': get_language(),
    }
