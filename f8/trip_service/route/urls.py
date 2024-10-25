from django.urls import path
from .views import RouteListView


urlpatterns = [
    path('routelist/', RouteListView.as_view()),
   
]


