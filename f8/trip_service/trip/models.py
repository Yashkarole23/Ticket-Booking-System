import random
from django.db import models
from route.models import Route

class Trip(models.Model):
    trip_id = models.CharField(max_length=255, primary_key=True, unique=True)  # Make trip_id the primary key
    user_id = models.CharField(max_length=255)  # Changed to CharField if needed
    vehicle_id = models.IntegerField()
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)  
    driver_name = models.CharField(max_length=255)
    trip_distance = models.FloatField()

    def save(self, *args, **kwargs):
        if not self.trip_id:  
            while True:
                
                random_number = random.randint(10000000, 99999999)
                self.trip_id = f"TP{random_number}"  

                # Check if the generated trip_id already exists
                if not Trip.objects.filter(trip_id=self.trip_id).exists():
                    break  # Unique ID found, exit the loop

        super().save(*args, **kwargs)

   