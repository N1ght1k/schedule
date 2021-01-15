from django.urls import path
from .views import index, schedule, flight_info

urlpatterns = [
    path('', index, name='index'),
    path('schedule/', schedule, name='schedule'),
    path('schedule/<str:flight_id>/', flight_info, name='flight'),
]