# Generated by Django 5.1.2 on 2024-10-21 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='route_stop',
        ),
    ]