import random
from django.db import models
from django.core.validators import RegexValidator

class Booking(models.Model):
    ticket_id = models.CharField(
        max_length=10,
        primary_key=True,
    )
    trip_id = models.CharField(
        max_length=10,
    )
    traveler_name = models.CharField(max_length=50)
    traveler_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^(?!0+$)\d{10}$', 'Invalid phone number. Must be a 10-digit number')]
    )
    ticket_cost = models.DecimalField(max_digits=10, decimal_places=2)
    traveler_email = models.EmailField()
    
    def save(self, *args, **kwargs):
        if not self.ticket_id: 
            while True:
                
                random_number = random.randint(10000000, 99999999)
                self.ticket_id = f"TK{random_number}"

                
                if not Booking.objects.filter(ticket_id=self.ticket_id).exists():
                    break  

        super().save(*args, **kwargs)

    