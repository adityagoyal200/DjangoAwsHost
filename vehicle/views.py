from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import vehicle,car,bike
from .serializers import vehicleSerializer,carSerializer,bikeSerializer

# Create your views here.
class vehicle(APIView):
    def get(request):
        vehicles = vehicleSerializer(vehicle.objects.all(),many=True)
        return Response(vehicles.data)
    
    def post(request):
        serializer = vehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)  
    
    def put(request,pk):
        vehicle = vehicle.objects.get(pk=pk)
        serializer = vehicleSerializer(vehicle,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(request,pk):
        vehicle = vehicle.objects.get(pk=pk)
        vehicle.delete()
        return Response("Vehicle deleted successfully")
    
    
class car(APIView):
    def get(request):
        cars = carSerializer(car.objects.all(),many=True)
        return Response(cars.data) 
    
    def post(request):
        serializer = carSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)    
    
    def put(request,pk):
        car = car.objects.get(pk=pk)
        serializer = carSerializer(car,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)  
    
    def delete(request,pk):
        car = car.objects.get(pk=pk)
        car.delete()
        return Response("Car deleted successfully") 
    
    
    
class bike(APIView):
    def get(request):
        bikes = bikeSerializer(bike.objects.all(),many=True)
        return Response(bikes.data) 
    
    def post(request):
        serializer = bikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(request,pk):
        bike = bike.objects.get(pk=pk)
        serializer = bikeSerializer(bike,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(request,pk):
        bike = bike.objects.get(pk=pk)
        bike.delete()
        return Response("Bike deleted successfully")    
    
    
        
        
        
