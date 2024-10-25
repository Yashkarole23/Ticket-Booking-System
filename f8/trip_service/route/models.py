import random
from django.db import models
from django.contrib.auth.models import User

class Route(models.Model):
    route_id = models.CharField(max_length=255, primary_key=True, unique=True)  
    user_id = models.CharField(max_length=255)  
    route_name = models.CharField(max_length=255)
    route_origin = models.CharField(max_length=255)
    route_destination = models.CharField(max_length=255)
    route_stops = models.JSONField(default=list)  
    
    def save(self, *args, **kwargs):
        if not self.route_id:  
            while True:
                
                random_number = random.randint(10000000, 99999999)
                self.route_id = f"RT{random_number}"

                
                if not Route.objects.filter(route_id=self.route_id).exists():
                    break  

        super().save(*args, **kwargs)

    def __str__(self):
        return self.route_name
