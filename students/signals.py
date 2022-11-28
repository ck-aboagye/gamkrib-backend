from django.db.models.signals import post_save
from django.contrib.auth.models import User
from students.models import *
from django.dispatch import receiver


#for profiles
@receiver(post_save, sender=Book)
def create_bookings(sender, instance, created, **kwargs):
    if created:
        Bookings.objects.create(booking=instance)


@receiver(post_save, sender=Book)
def save_bookings(sender, instance, **kwargs):
    instance.bookings.save()

