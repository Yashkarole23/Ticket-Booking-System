from django.urls import path
from .views import TripListView

urlpatterns = [
    path('triplists/', TripListView.as_view()),

]