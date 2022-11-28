from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.

class CustomUser(AbstractUser):
    is_landlord = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=100)
    school = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    school_id = models.CharField(max_length=100, null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    level = models.CharField(max_length=100, null=True, blank=True)

    # LANDLORDS DETAILS
    location = models.CharField(max_length=100, null=True, blank=True)
    ID_card = models.CharField(max_length=100, null=True, blank=True)
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=100)
    school = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    school_id = models.CharField(max_length=100, null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    level = models.CharField(max_length=100, null=True, blank=True)

    # LANDLORDS DETAILS
    ID_card = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    


    def save(self, *args, **kwargs):
        self.id = self.user.id
        self.username = self.user.username
        self.email = self.user.email
        self.phone_number = self.user.phone_number
        self.school = self.user.school
        self.school_id = self.user.school_id
        self.department = self.user.department
        self.course = self.user.course
        self.level = self.user.level

        #LANDLORDS DETAILS
        self.ID_card = self.user.ID_card
        self.location = self.user.location
        

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} Profile'



    

