from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin
from sass_processor.processor import sass_processor
from django.conf import settings

from .models import Document
# Register your models here.

class DocumentAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_per_page = 20
    list_display = ['order', 'image_preview', 'title_en', 'product_type', 'document_type' ]
    list_display_links = ['image_preview', 'title_en', ]

    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<div><img src="{url}"/></div>'.format(url=obj.image.url))
        else:
            return mark_safe('<div><img src="' + settings.STATIC_URL + 'images/document.jpg"/></div>')

    class Media:
        css = {'all': (sass_processor('scss/admin.scss'),)}

admin.site.register(Document, DocumentAdmin)
