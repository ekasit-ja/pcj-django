from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import Finance
# Register your models here.

class FinanceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_per_page = 20
    list_display = ['order', 'short_title_en', 'short_content_en' ]
    list_display_links = ['short_title_en', 'short_content_en', ]

admin.site.register(Finance, FinanceAdmin)
