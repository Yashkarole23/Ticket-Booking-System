# Generated by Django 5.1.2 on 2024-10-24 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='user_id',
            field=models.CharField(max_length=255),
        ),
    ]
