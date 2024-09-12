from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from profiles.models import UserProfile


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
MONTH = 30 * DAY

# Create your models here.
class Category(models.Model):
    """
    Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value
    """
    
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Create your models here.
class Product(models.Model):
    """
    Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value
    """
    
    class Meta:
        verbose_name_plural = 'Products'

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    acoustic_type = models.CharField(max_length=254)
    size = models.CharField(max_length=254, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    stock = models.DecimalField(max_digits=6, decimal_places=0, default=0)

    def __str__(self):
        return self.name


# Create your models here.
class RentalProduct(models.Model):
    """
    Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value
    """
    
    class Meta:
        verbose_name_plural = 'Rentals'

    product = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL)
    rental_sku = models.CharField(max_length=254, null=True, blank=True)
    rental_price = models.DecimalField(max_digits=6, decimal_places=2)
    rental_period = models.DateField()
    rental_stock = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    has_premium = models.BooleanField(default=False, null=True, blank=True)
    premium = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.rental_sku


class Bid(models.Model):
    """
    Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value
    """
    
    buyer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='auction_buyer')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

# Create your models here.	
class AuctionProduct(models.Model):
    """
    Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value
    """
    
    class Meta:
        verbose_name_plural = 'Auctions'

    CONDITION = (
        ('new', 'New / Never Opened'),
        ('refurbished', 'Refurbished'),
        ('mint_condition', 'Mint Condition'),
        ('good_condition', 'Good Condition'),
        ('poor_condition', 'Poor Condition'),
    )

    title = models.CharField(max_length=254)
    description = models.TextField()
    instrument = models.CharField(max_length=254, default="")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    condition = models.CharField(max_length=20, choices=CONDITION)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    auction_period = models.DateField()
    purchased = models.BooleanField(default=False, null=True, blank=True)
    seller = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='auction_seller')
    owner = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE)
    bidders = models.ForeignKey('Bid', on_delete=models.SET_NULL, null=True, blank=True, related_name='bid')

    @property
    def remaining_days(self):
        remaining_days = (self.auction_period - datetime.now().date()).days
        return remaining_days

    def __str__(self):
        return self.title



