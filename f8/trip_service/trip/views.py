import json
import requests # type: ignore
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Trip
from route.models import Route

@method_decorator(csrf_exempt, name='dispatch')
class TripListView(View):

    def post(self, request):
        try:
            data = json.loads(request.body.decode("utf-8"))
            user_id = data.get('user_id')
            vehicle_id = data.get('vehicle_id')
            route_id = data.get('route_id')
            driver_name = data.get('driver_name')
            trip_distance = data.get('trip_distance')

          
            try:
                route_instance = Route.objects.get(route_id=route_id)
            except Route.DoesNotExist:
                return JsonResponse({"error": "Route does not exist."}, status=400)

           
            trip = Trip(
                user_id=user_id,
                vehicle_id=vehicle_id,
                route_id=route_instance,
                driver_name=driver_name,
                trip_distance=trip_distance
            )
            trip.save()

            
            booking_response = self.create_booking(user_id, trip.trip_id)

            response_data = {
                "message": "Trip created successfully.",
                "trip_id": trip.trip_id,
                "booking_response": booking_response
            }
            return JsonResponse(response_data, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def create_booking(self, user_id, trip_id):
        booking_url = "http://localhost:9000/api/bookings/"
        payload = {
            "user_id": user_id,
            "trip_id": trip_id
        }
           
        try:
            response = requests.post(booking_url, json=payload)
            response.raise_for_status()  
            return response.json() 
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get(self, request):
        trips = Trip.objects.all()

        
        page_number = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 2)

        paginator = Paginator(trips, page_size)
    
        try:
            page_trips = paginator.page(page_number)
        except PageNotAnInteger:
            page_trips = paginator.page(1)  
        except EmptyPage:
            page_trips = paginator.page(paginator.num_pages)  

        items_data = []
        for trip in page_trips:
            items_data.append({
                'trip_id': trip.trip_id,
                'user_id': trip.user_id,
                'vehicle_id': trip.vehicle_id,
                'route_id': trip.route_id.route_id,
                'driver_name': trip.driver_name,
                'trip_distance': trip.trip_distance,
            })

        response_data = {
            'TripList': items_data,
            'total': paginator.count,
            'page': page_number,
            'page_size': page_size,
            'total_pages': paginator.num_pages,
        }

        return JsonResponse(response_data, status=200)
