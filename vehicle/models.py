from django.db import models

# Create your models here.
class vehicle(models.Model):
    vehicle_type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class car(models.Model):
    name = models.CharField(max_length=50)
    car_type = models.OneToOneField(vehicle, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    
class bike(models.Model):
    name = models.CharField(max_length=50)
    bike_type = models.OneToOneField(vehicle, on_delete=models.CASCADE, related_name='bikes')
    created_at = models.DateTimeField(auto_now_add=True)    

