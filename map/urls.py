from django.urls import path
from . import views
from . import views

app_name = "map"

urlpatterns = [
    path('', views.index, name='index'),
    # path("", MapView.as_view()),
]
