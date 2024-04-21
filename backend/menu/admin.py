from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'url',
                    'parent',
                    'named_url')
    fields = ['name', 'url', 'parent', 'named_url']

    list_filter = ['name']

    empty_value_display = '-пусто-'
