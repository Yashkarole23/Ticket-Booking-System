# booking/urls.py

from django.urls import path
from .views import BookingListView  # Ensure this matches the defined view class

urlpatterns = [
    path('bookings/', BookingListView.as_view(), name='booking_list'),
]
