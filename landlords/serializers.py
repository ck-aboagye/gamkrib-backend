from rest_framework import serializers
from .models import *



class ListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listings
        fields = '__all__'


class WithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdrawal
        fields = '__all__'