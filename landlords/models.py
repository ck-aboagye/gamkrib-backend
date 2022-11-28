from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


# Create your models here.


class Listings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    image = models.CharField(max_length=100)
    number_of_persons = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} listing'




class Withdrawal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0, null =True)




