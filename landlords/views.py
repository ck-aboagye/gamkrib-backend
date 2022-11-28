from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
from rest_framework.decorators import api_view
from uritemplate import partial
from .serializers import *
from students.serializers import *
from . models import *
from .filters import ListingFilter

from students.models import *
# Create your views here.   

# Create your views here.



@api_view(['POST'])
def ListingsCreate(request):
    #if request.user.is_landlord == True:

        if request.method == "POST":

            serializer = ListingsSerializer(data=request.data)
            
        if serializer.is_valid():
                
            serializer.save()

        return Response(serializer.data)



@api_view(['GET'])
def ListingsView(request):
   
    queryset = Listings.objects.all()
    filterset = ListingFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
         queryset = filterset.qs
    serializer = ListingsSerializer(queryset, many=True)
    
    return Response(serializer.data)



@api_view(['GET'])
def ListingsDetail(request, pk):
    listings = Listings.objects.get(id=pk)
    serializer = ListingsSerializer(listings, many=False)
    return Response(serializer.data)


#@login_required
@api_view(['GET'])
def MyListings(request, pk):
    permission_classes = [IsAuthenticated]
    my_listings = Listings.objects.filter(user=pk)
    serializer = ListingsSerializer(my_listings, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def BookingsList(request, pk):
    permission_classes = [IsAuthenticated]
    bookings = Bookings.objects.filter(owner=pk)
    serializer = BookingsSerializer(bookings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TenantBookingsList(request, pk):
    permission_classes = [IsAuthenticated]
    bookings = Bookings.objects.filter(user=pk)
    serializer = BookingsSerializer(bookings, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def TenantBookingsUpdate(request, pk):
    #permission_classes = [IsAuthenticated]
    bookings = Bookings.objects.get(id=pk)
    if request.method == 'PUT':

        serializer = BookingsSerializer(instance=bookings, data=request.data, many = False, partial=True)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['POST'])
def  WithdrawalView(request):
    if request.method == "POST":
        serializer = WithdrawalSerializer(data=request.data)
            
    if serializer.is_valid():
                
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def  WithdrawalListView(request,pk):
    withdrawals = Withdrawal.objects.filter(user=pk)
    serializer = WithdrawalSerializer(withdrawals, many=True)

    return Response(serializer.data)




