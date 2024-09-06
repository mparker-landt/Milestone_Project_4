from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime

# Create your models here.
class Enquiry(models.Model):
    """
    A user profile model for maintaining shipping
    delivery information and order history
    """
    SUBJECT_CHOICE = (
        ('general', 'General Enquiry'),
        ('return', 'Product Return'),
        ('auction', 'Auction Enquiry'),
        ('rental', 'Rental Enquiry'),
        ('career', 'Career Interest'),
    )

    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICE, default='general')
    message = models.CharField(max_length=80, default='', blank=False)
    signup = models.BooleanField(max_length=1, default=False, null=False, blank=False)
    create_date = models.DateField(null=False, blank=False, auto_now_add=True)

    def __str__(self):
        return self.message