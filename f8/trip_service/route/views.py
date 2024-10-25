import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Route

@method_decorator(csrf_exempt, name='dispatch')
class RouteListView(View):

    def post(self, request):
        try:
            data = json.loads(request.body.decode("utf-8"))
            user_id = data.get('user_id')
            route_name = data.get('route_name')
            route_origin = data.get('route_origin')
            route_destination = data.get('route_destination')
            route_stops = data.get('route_stops', [])

            route = Route(
                user_id=user_id,
                route_name=route_name,
                route_origin=route_origin,
                route_destination=route_destination,
                route_stops=route_stops
            )
            route.save()

            response_data = {
                "message": "Route created successfully.",
                "route_id": route.route_id
            }
            return JsonResponse(response_data, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def get(self, request):
        routes = Route.objects.all()
        items_data = []

        for route in routes:
            items_data.append({
                'route_id': route.route_id,
                'user_id': route.user_id,
                'route_name': route.route_name,
                'route_origin': route.route_origin,
                'route_destination': route.route_destination,
                'route_stops': route.route_stops
            })

        return JsonResponse({'RouteList': items_data}, status=200)
