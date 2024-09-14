from django.contrib import admin
from .models import Category, Product, AuctionProduct, RentalProduct


class CategoryAdmin(admin.ModelAdmin):
    """ Fields for Cateogry Model to show on admin page """

    list_display = (
        'name',
        'friendly_name'
    )


class ProductAdmin(admin.ModelAdmin):
    """Fields for Product Model to show on admin page"""

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
    """ Fields for Rental Model to show on admin page """

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
    """ Fields for Auction Model to show on admin page """

    list_display = (
        'title',
        'description',
        'instrument',
        'image',
        'condition',
        'base_price',
        'auction_price',
        'auction_period',
        'purchased',
        'owner',
        'bidders'
    )

    ordering = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(RentalProduct, RentalAdmin)
admin.site.register(AuctionProduct, AuctionAdmin)
