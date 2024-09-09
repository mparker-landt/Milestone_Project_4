from django.contrib import admin
from .models import Category, Product, AuctionProduct, RentalProduct

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
        'stock'
    )

    ordering = ('sku',)

class RentalAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'rental_sku',
        'rental_price',
        'rental_period',
        'rental_stock',
        'has_premium',
        'premium'
    )

    ordering = ('rental_sku',)

class AuctionAdmin(admin.ModelAdmin):
    list_display = (
        'auction_id',
        'title',
        'description',
        'image',
        'condition',
        'base_price',
        'auction_price',
        'auction_period',
        'purchased',
        'seller'
    )

    ordering = ('auction_id',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(RentalProduct, RentalAdmin)
admin.site.register(AuctionProduct, AuctionAdmin)