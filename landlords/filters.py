from . models import *
import django_filters

class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Listings
        fields = ['location', 'price', 'number_of_persons', 'user']