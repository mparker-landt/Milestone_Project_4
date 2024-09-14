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


class Category(models.Model):
    """ Category model that has instrument category names """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Product model that has main store product details """

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


class RentalProduct(models.Model):
    """ Rental model that has rental store product details """

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


class AuctionProduct(models.Model):
    """ Auction model that has auction store product details """

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
    auction_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    auction_period = models.DateField()
    purchased = models.BooleanField(default=False, null=True, blank=True)
    owner = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE)
    bidders = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='bid')

    @property
    def remaining_days(self):
        """ Calculates remaining days from today until auction period date """
        remaining_days = (self.auction_period - datetime.now().date()).days
        return remaining_days

    def __str__(self):
        return self.title
