import uuid
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

    class Meta:
        verbose_name_plural = 'Enquiries'

    SUBJECT_CHOICE = (
        ('general', 'General Enquiry'),
        ('return', 'Product Return'),
        ('auction', 'Auction Enquiry'),
        ('rental', 'Rental Enquiry'),
        ('career', 'Career Interest'),
    )

    enquiry_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICE, default='general')
    message = models.CharField(max_length=80, default='', blank=False)
    signup = models.BooleanField(max_length=1, default=False, null=False, blank=False)
    create_date = models.DateField(default=datetime.date.today ,null=False, blank=False)

    def _generate_enquiry_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.enquiry_number:
            self.enquiry_number = self._generate_enquiry_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.enquiry_number