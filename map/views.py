from doctest import script_from_examples
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.template import loader
from lessons_widget.models import Lesson

# class MapView(TemplateView):
#     template_name: "map.html"

def index(request):
    # return HttpResponse("Welcome to the Map index page. Currently in development.")
    latest_lessons_list = Lesson.objects.order_by('title')[:15]
    template = loader.get_template('map/map.html')
    context = {
        'latest_lessons_list': latest_lessons_list,
    }
    return HttpResponse(template.render(context, request))
