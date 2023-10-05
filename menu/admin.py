from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['menu_name', 'title', 'url', 'named_url', 'parent']

admin.site.register(MenuItem, MenuItemAdmin)
