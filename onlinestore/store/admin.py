from django.contrib import admin
from store.models import Category, Item

class ItemAdmin (admin.ModelAdmin):
	list_display = ('item_text', 'category', 'price')

admin.site.register(Item, ItemAdmin)
admin.site.register(Category)

