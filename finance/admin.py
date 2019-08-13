from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import Finance
# Register your models here.

class FinanceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_per_page = 10

admin.site.register(Finance, FinanceAdmin)
