from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
from rest_framework.decorators import api_view
from uritemplate import partial
from .serializers import *
from . models import *

# Create your views here.


@api_view(['POST'])
def BookCreate(request):
    if request.method == "POST":

        serializer = BookSerializer(data=request.data)
        
    if serializer.is_valid():
            
        serializer.save()

    return Response(serializer.data)



@login_required
@api_view(['GET'])
def BookList(request):
    #permission_classes = [IsAuthenticated]
    bookings = Book.objects.filter(user=request.user)
    serializer = BookSerializer(bookings, many=True)
    return Response(serializer.data)