from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from landlords.models import Listings
# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)
    image = models.CharField(max_length=100, blank=True)
    number_of_persons = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    price = models.CharField(max_length=100, blank=True)
    #checked_in = models.BooleanField(default=False)
    owner = models.PositiveIntegerField(blank=True)

    
    
    def save(self, *args, **kwargs):
        self.image = self.listing.image
        self.number_of_persons = self.listing.number_of_persons
        self.location = self.listing.location
        self.description = self.listing.description
        self.price = self.listing.price
        self.owner = self.listing.user.id
        
     

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} booking'


class Bookings(models.Model):
    booking = models.OneToOneField(Book, on_delete=models.CASCADE)

    user = models.PositiveIntegerField(blank=True)
    image = models.CharField(max_length=100, blank=True)
    number_of_persons = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    price = models.CharField(max_length=100, blank=True)
    checked_in = models.BooleanField(default=False)
    owner = models.PositiveIntegerField(blank=True)



    def save(self, *args, **kwargs):
        self.user = self.booking.user.id
        self.image = self.booking.listing.image
        self.number_of_persons = self.booking.listing.number_of_persons
        self.location = self.booking.listing.location
        self.description = self.booking.listing.description
        self.price = self.booking.listing.price
        #self.checked_in = self.booking.checked_in
        self.owner = self.booking.owner
        
     

        super().save(*args, **kwargs)

    


    def __str__(self):
        return f'{self.booking.id} booked'
