from django.db import models
from django.utils import timezone
import datetime
from profiles.models import UserProfile

# Create your models here.
class Category(models.Model):
    
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
class AuctionProduct(models.Model):
    
    class Meta:
        verbose_name_plural = 'Auctions'

    product = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL)
    seller = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='auction')
    # buyers = ArrayField(models.CharField(max_length=), blank=True)
    auction_id = models.CharField(max_length=254, null=True, blank=True)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    auction_price = models.DecimalField(max_digits=6, decimal_places=2)
    auction_period = models.DecimalField(max_digits=6, decimal_places=0)
    purchased = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.seller


# Create your models here.
class RentalProduct(models.Model):
    
    class Meta:
        verbose_name_plural = 'Rentals'

    product = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL)
    renter = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='rental')
    rental_sku = models.CharField(max_length=254, null=True, blank=True)
    rental_price = models.DecimalField(max_digits=6, decimal_places=2)
    rental_period = models.DateField()
    rental_stock = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    premium = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.seller

"""
Violin
Viola
Cello
Double Bass
Harp
Guitar
Bass Guitar

Trumpet
French Horn
Euphonium
Tuba
Cornet
Flugelhorn
Tenor Horn
Baritone Horn
Sousaphone
Mellophone

Piccolo
Flute
Oboe
English Horn
Clarinet
E-Flat Clarinet
Bass Clarinet
Bassoon
Contrabassoon

Drum Kit

Keyboard
"""