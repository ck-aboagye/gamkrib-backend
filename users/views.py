from urllib import request
from django.shortcuts import render
from .models import *
User = settings.AUTH_USER_MODEL
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required 
from rest_framework.decorators import api_view
from .serializers import *
from . models import *
from dj_rest_auth.registration.views import RegisterView
# Create your views her




@api_view(['GET'])
def ProfileView(request):
    permission_classes = [IsAuthenticated]
   # user = request.user.pk
    profile = Profile.objects.filter(user=request.user)
    serializer = UserProfileSerializer(profile, many=True)

    return Response(serializer.data)