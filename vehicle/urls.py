from django.urls import path 


urlpatterns = [
    path('vehicle/',views.vehicle_list,name='vehicle_list'),
    path('vehicle/<int:pk>/',views.vehicle_detail,name='vehicle_detail'),
    path('car/',views.car_list,name='car_list'),
    path('car/<int:pk>/',views.car_detail,name='car_detail'),
    path('bike/',views.bike_list,name='bike_list'),
    path('bike/<int:pk>/',views.bike_detail,name='bike_detail'),
]