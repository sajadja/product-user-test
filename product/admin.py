from django.contrib import admin
from django.contrib.admin import register

from product.models import Product


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['name']
