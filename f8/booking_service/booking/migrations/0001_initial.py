# Generated by Django 5.1.2 on 2024-10-23 09:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('ticket_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('trip_id', models.CharField(max_length=10)),
                ('traveler_name', models.CharField(max_length=50)),
                ('traveler_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^(?!0+$)\\d{10}$', 'Invalid phone number. Must be a 10-digit number')])),
                ('ticket_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('traveler_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
