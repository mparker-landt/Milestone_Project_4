from django.contrib import admin
from .models import Category, Product, AuctionProduct, RentalProduct

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    """
    Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value
    """
    
    list_display = (
        'name',
        'friendly_name'
    )

class ProductAdmin(admin.ModelAdmin):
    """
    Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value
    """
    
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
    """
    Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value
    """
    
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
    """
    Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value
    """
    
    list_display = (
        'title',
        'description',
        'instrument',
        'image',
        'condition',
        'base_price',
        'auction_period',
        'purchased',
        'seller',
        'owner',
        'bidders'
    )

    ordering = ('title',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(RentalProduct, RentalAdmin)
admin.site.register(AuctionProduct, AuctionAdmin)