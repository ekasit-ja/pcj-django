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
            ('projects', reverse('project:project-list')),
            ('news', reverse('news:news-list')),
            ('contact', reverse('page:page-contact')),
            ('career', reverse('page:page-career')),
            ('en', '/en' + request.get_full_path()[3:], 'images/flag_en.png'),
            ('th', '/th' + request.get_full_path()[3:], 'images/flag_th.png'),
        ],
        'navbar_dropdown_items': [
            ('frd-&-non-frd', reverse('page:page-home'), 'images/fire_doors.jpg'),
            ('fdc', reverse('page:page-home'), 'images/fire_dampers.jpg'),
            ('fsd-ul', reverse('page:page-home'), 'images/fsd_ul.jpg'),
            ('ddp', reverse('page:page-home'), 'images/duct_dampers.jpg'),
            ('ds', reverse('page:page-home'), 'images/duct_silencers.jpg'),
            ('aol', reverse('page:page-home'), 'images/air_outlets.jpg'),
        ],
        'LANG': get_language(),
        'PHONE1_en': '+66 2 279 4166',
        'PHONE1_th': '02 279 4166',
        'PHONE2_en': '+66 2 616 0184',
        'PHONE2_th': '02 616 0184',
        'FAX_en': '+66 2 616 0071',
        'FAX_th': '02 616 0071',
        'PHONE_FACTORY_en': '+66 36 262 333',
        'PHONE_FACTORY_th': '036 262 333',
        'FAX_FACTORY_en': '+66 36 262 334',
        'FAX_FACTORY_th': '036 262 334',
        'EMAIL_SALES': 'sales@pcjindustries.co.th',
        'EMAIL_CAREER': 'careers@pcjindustries.co.th',
        'FACEBOOK': "https://www.facebook.com/pcjindustries/",
        'YOUTUBE': "https://www.youtube.com/channel/UCGl6i4eh4_ctQNTyeiIPssQ",
    }
