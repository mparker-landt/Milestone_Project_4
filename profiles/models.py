from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """ UserProfile model that has personal user, shipping and billing details """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_title = models.CharField(max_length=20, null=True, blank=True)
    user_firstname = models.CharField(max_length=50, null=True, blank=True)
    user_surname = models.CharField(max_length=50, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_email = models.CharField(max_length=50, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)
    shipping_postcode = models.CharField(max_length=20, null=True, blank=True)
    shipping_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    shipping_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    shipping_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    shipping_county = models.CharField(max_length=80, null=True, blank=True)
    billing_postcode = models.CharField(max_length=20, null=True, blank=True)
    billing_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    billing_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    billing_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    billing_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Creates/updates a user profile on request """

    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
