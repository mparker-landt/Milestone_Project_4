from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculates cost for a number of products
    
    Keyword arguments:
    price -- (float) cost of a product
    quantity -- (integer) how many of a certain product have been chosen
    Return: (float) total cost for the numbers of a certain product
    """
    
    return price * quantity