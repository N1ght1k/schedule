from django.shortcuts import render
from django.http import JsonResponse
from .serializers import DepartureSerializer, ArrivalSerializer
from .models import Departure, Arrival
from datetime import datetime, timedelta

def index(request):
    return render(request, 'flight_schedule/index.html')

def schedule(request):
    return render(request, 'flight_schedule/schedule.html')


def dep_flights(request, date='today'):
    if request.method == 'GET':
        now = datetime.now()
        yesterday = now - timedelta(days=1)
        tomorrow = now + timedelta(days=1)
        if date == 'yesterday':
            flights = Departure.objects.filter(flight_time__day=yesterday.day)
            serializer = DepartureSerializer(flights, many=True)
            return JsonResponse(serializer.data, safe=False)
        elif date == 'tomorrow':
            flights = Departure.objects.filter(flight_time__day=tomorrow.day)
            serializer = DepartureSerializer(flights, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            flights = Departure.objects.filter(flight_time__day=now.day)
            serializer = DepartureSerializer(flights, many=True)
            return JsonResponse(serializer.data, safe=False)


def arr_flights(request, date='today'):
    if request.method == 'GET':
        now = datetime.now()
        yesterday = now - timedelta(days=1)
        tomorrow = now + timedelta(days=1)
        if date == 'yesterday':
            flights = Arrival.objects.filter(flight_time__day=yesterday.day)
            serializer = ArrivalSerializer(flights, many=True)
            return JsonResponse(serializer.data, safe=False)
        elif date == 'tomorrow':
            flights = Arrival.objects.filter(flight_time__day=tomorrow.day)
            serializer = ArrivalSerializer(flights, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            flights = Arrival.objects.filter(flight_time__day=now.day)
            serializer = ArrivalSerializer(flights, many=True)
            return JsonResponse(serializer.data, safe=False)


def flight_info(request, flight_id):
    if Arrival.objects.filter(flight_id = flight_id).exists():
        flight = Arrival.objects.get(flight_id = flight_id)
        context = {'flight_info': flight}
        return render(request, 'flight_schedule/flight_info_arr.html', context)
    if Departure.objects.filter(flight_id = flight_id).exists():
        flight = Departure.objects.get(flight_id = flight_id)
        context = {'flight_info': flight}
        return render(request, 'flight_schedule/flight_info_dep.html', context)
