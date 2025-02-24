from rest_framework import serializers
from .models import vehicle,car,bike

class vehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicle
        fields = '__all__'
        
class carSerializer(serializers.ModelSerializer):
    vehicle_data = vehicleSerializer(source='vehicle',read_only=True)
    class Meta:
        model = car
        fields = '__all__'
        
class bikeSerializer(serializers.ModelSerializer):  
    vehicle_data = vehicleSerializer(source='vehicle',read_only=True)
    class Meta:
        model = bike
        fields = '__all__'
        
        
        
