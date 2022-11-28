from email.policy import default
from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from . models import *

from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.serializers import PasswordResetSerializer
from django.conf import settings

from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=100)
    school = serializers.CharField(max_length=100, default="")
    department = serializers.CharField(max_length=100, default="")
    school_id = serializers.CharField(max_length=100, default="")
    course = serializers.CharField(max_length=100, default="")
    level = serializers.CharField(max_length=100, default="")
    
    is_landlord = serializers.BooleanField(default=False)

    #LANDLORDS DETAILS
    ID_card = serializers.CharField(max_length=100, default="")
    location = serializers.CharField(max_length=100, default="")

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['phone_number'] = self.validated_data.get('phone_number', '')
        data_dict['school'] = self.validated_data.get('school', '')
        data_dict['school_id'] = self.validated_data.get('school_id', '')
        data_dict['level'] = self.validated_data.get('level', '')
        data_dict['course'] = self.validated_data.get('course', '')
        data_dict['department'] = self.validated_data.get('department', '')
        
        data_dict['is_landlord'] = self.validated_data.get('is_landlord', '')
        
        #LANDLORDS DETAILS
        data_dict['location'] = self.validated_data.get('location', '')
        data_dict['ID_card'] = self.validated_data.get('ID_card', '')

        return data_dict


class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + \
            ('phone_number','school', 'school_id', 'level', 'course', 'department', 'is_landlord','location', 'ID_card')



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

