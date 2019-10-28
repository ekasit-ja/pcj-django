from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin
from sass_processor.processor import sass_processor

from .models import News
# Register your models here.

class NewsAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_per_page = 20
    list_display = ['order', 'short_title_en', 'short_content_en', 'image_preview', ]
    list_display_links = ['short_title_en', 'image_preview', ]

    def image_preview(self, obj):
        return mark_safe('<div><img src="{url}"/></div>'.format(url=obj.image.url))

    class Media:
        css = {'all': [sass_processor('scss/admin.scss'),]}

admin.site.register(News, NewsAdmin)
