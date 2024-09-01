from django.contrib import admin
from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name'
    )

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'size',
        'acoustic_type',
        'image',
        'purchased'
    )

    ordering = ('sku',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)