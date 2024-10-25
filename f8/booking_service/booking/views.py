import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Booking

@method_decorator(csrf_exempt, name='dispatch')
class BookingListView(View):
    
    def post(self, request):
        try:
            data = json.loads(request.body.decode("utf-8"))
            trip_id = data.get('trip_id')
            traveler_name = data.get('traveler_name')
            traveler_number = data.get('traveler_number')
            ticket_cost = data.get('ticket_cost')
            traveler_email = data.get('traveler_email')

            
            booking = Booking(
                trip_id=trip_id,
                traveler_name=traveler_name,
                traveler_number=traveler_number,
                ticket_cost=ticket_cost,
                traveler_email=traveler_email
            )
            booking.save()  

            response_data = {
                "message": "Booking created successfully.",
                "ticket_id": booking.ticket_id
            }
            return JsonResponse(response_data, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def get(self, request):
        bookings = Booking.objects.all()
        items_data = []

        for booking in bookings:
            items_data.append({
                'ticket_id': booking.ticket_id,
                'trip_id': booking.trip_id,
                'traveler_name': booking.traveler_name,
                'traveler_number': booking.traveler_number,
                'ticket_cost': str(booking.ticket_cost),  
                'traveler_email': booking.traveler_email,
            })

        return JsonResponse({'BookingList': items_data}, status=200)
