from collections import defaultdict
from django.shortcuts import render
from django.http import JsonResponse
from .models import Trip

def index(request):
    return render(request, 'home.html')

def list_cities(request):
    cities = Trip.objects.all()
    categories_dict = defaultdict(list)
    for item in list(cities.values()):
        categories_dict[item['category']].append(item)
    return JsonResponse(dict(categories_dict))