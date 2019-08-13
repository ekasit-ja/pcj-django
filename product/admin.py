from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin
from sass_processor.processor import sass_processor

from .models import Product
# Register your models here.

class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_per_page = 10
    list_display = ['order', 'title_en', 'image_preview', 'product_type', ]
    list_display_links = ['title_en', 'image_preview', ]

    def image_preview(self, obj):
        return mark_safe('<div><img src="{url}"/></div>'.format(url=obj.image.url))

    class Media:
        css = {'all': [sass_processor('scss/admin.scss'),]}

admin.site.register(Product, ProductAdmin)
