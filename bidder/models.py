from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from .services import localization_service
from .services.user_service import BidderUserManager


class Property(models.Model):
    address = models.CharField(max_length=200)
    uploaded_date = models.DateTimeField("date uploaded", default=timezone.now)
    minimum_increment = models.IntegerField(default=500)
    link = models.TextField(blank=True, default="")
    image = models.ImageField(upload_to='property_images/', blank=True)

    class Meta:
        permissions = [
            ('view_bids', 'Can view all bids'),
        ]

    def __str__(self):
        return self.address


class BidUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    viewable_properties = models.ManyToManyField(Property, related_name='viewable_by_users')

    objects = BidderUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Bid(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(BidUser, on_delete=models.CASCADE)
    bid = models.IntegerField()
    timestamp = models.DateTimeField("date bid", default=timezone.now)

    def bid_to_str(self):
        return localization_service.format_number_as_pound_value_commas(self.bid)
