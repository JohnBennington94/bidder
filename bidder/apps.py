"""Generic base Django app Config"""

from django.apps import AppConfig


class BidderConfig(AppConfig):
    """Custom App Config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bidder'
