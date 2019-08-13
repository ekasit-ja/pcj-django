from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from django.forms import Textarea
from django.db import models
from sass_processor.processor import sass_processor

from .models import News, NewsImage
# Register your models here.

class NewsImageInline(SortableInlineAdminMixin, admin.TabularInline):
    fields = ['order', 'image_preview', 'image', ]
    readonly_fields = ('image_preview',)
    model = NewsImage
    extra = 1

    def image_preview(self, obj):
        return mark_safe('<div><img src="{url}"/></div>'.format(url=obj.image.url))

class NewsAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['order', 'short_title_en', 'short_content_en',]
    list_display_links = ['short_title_en', ]
    inlines = [NewsImageInline]

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':3})},
    }

    class Media:
        css = {'all': [sass_processor('scss/admin.scss'),]}

admin.site.register(News, NewsAdmin)



class NewsImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['order', 'image_preview', 'news_id', 'news', ]
    list_display_links = ['image_preview', ]

    def image_preview(self, obj):
        return mark_safe('<div><img src="{url}"/></div>'.format(url=obj.image.url))

    class Media:
        css = {'all': [sass_processor('scss/admin.scss'),]}

admin.site.register(NewsImage, NewsImageAdmin)
