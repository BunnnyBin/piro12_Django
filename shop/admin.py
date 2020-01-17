from django.contrib import admin
from .models import Item   # shop앱의 Item모델

# admin.site.register(Item)  # Item이 사이트에 뜨게하도록

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'short_desc', 'price', 'is_publish']
    list_display_links = ['name']
    list_filter = ['is_publish', 'updated_at']
    search_fields = ['name']

    def short_desc(self, item):
        return item.desc[:20]