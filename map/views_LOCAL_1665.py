from doctest import script_from_examples
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to the Map index page. Currently in development.")

def maps_view(request):
      
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "./templates/map.html")