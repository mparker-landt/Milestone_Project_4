from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from store.models import Product

def cart_contents(request):
    """
    Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value
    """

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    delivery = Decimal(9.95) #total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    # free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    grand_total = delivery + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        # 'free_delivery_delta': free_delivery_delta,
        # 'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

def cart_quantity(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})