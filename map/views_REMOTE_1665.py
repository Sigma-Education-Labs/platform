from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from lessons_widget.models import Lesson

def index(request):
    latest_lessons_list = Lesson.objects.order_by('title')[:15]
    template = loader.get_template('.templates/map.html')
    context = {
        'latest_lessons_list': latest_lessons_list,
    }
    return HttpResponse(template.render(context, request))
