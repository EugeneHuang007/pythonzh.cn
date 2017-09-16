from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mptt.admin import MPTTModelAdmin

from .models import Category


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    date_hierarchy = 'created'
    list_display = ('name', 'parent', 'slug', 'rank', 'created', 'modified', 'is_visible', 'show')

    def is_visible(self, obj):
        return not obj.is_removed

    is_visible.short_description = _("Is visible")
    is_visible.boolean = True
