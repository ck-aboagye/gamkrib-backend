
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from landlords import views
from students import views as student_views
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    #re_path('.*', TemplateView.as_view(template_name='index.html')),
    path(('users/'), include('users.urls')),
   
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
   

   path('listings-create/', views.ListingsCreate, name = "listings-create"),
   path('listings/', views.ListingsView, name = "listings"),
   path('listings/<str:pk>', views.ListingsDetail, name = "listings-detail"),
   path('my-listings/<str:pk>', views.MyListings, name = "my-listings"),


   path('bookings/', student_views.BookList, name = "bookings"),
   path('book-create/', student_views.BookCreate, name = "book-create"),


    path('my-bookings/<str:pk>', views.BookingsList, name = 'landlord-bookings-list'),
    path('my-bookings-tenant/<str:pk>', views.TenantBookingsList, name='tenant-bookings-list'),
    path('my-bookings-tenant-update/<str:pk>', views.TenantBookingsUpdate, name ='tenant-bookings-update'),


    path('withdrawal/', views.WithdrawalView, name = "withdrawal"),
    path('withdrawal-list/<str:pk>', views.WithdrawalListView, name = "withdrawal-list")
]
