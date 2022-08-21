from doctest import script_from_examples
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from lessons_widget.models import Lesson # , Snippet
# from lessons_widget.forms import SnippetForm

# class MapView(TemplateView):
#     template_name: "map.html"

def index(request):
    # return HttpResponse("Welcome to the Map index page. Currently in development.")
    latest_lessons_list = Lesson.objects.order_by('title')[:15]
    template = loader.get_template('map/map.html')
    
    # if request.method == 'POST':
    #     form = SnippetForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    # else:
    #     form = SnippetForm()

    context = {
        'latest_lessons_list': latest_lessons_list,
        # "form": form,
        # "snippets": Snippet.objects.all()
    }
    return HttpResponse(template.render(context, request))
