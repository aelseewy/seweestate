from django.shortcuts import render, redirect
from .models import Team
from listings.models import Post
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    teams = Team.objects.all()
    #featured_cars =Car.objects.order_by('-created_date').filter(is_featured=True)
    #all_cars = Car.objects.order_by('-created_date')
    #model_search = Car.objects.values_list('model', flat=True).distinct()
    #city_search = Car.objects.values_list('city', flat=True).distinct()
    #year_search = Car.objects.values_list('year', flat=True).distinct()
    #body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    # search_fields = Car.objects.values('model', 'city', 'year', 'body_style')
    template = 'core/home.html'

    data = {
        'teams' : teams,

    }

    return render(request, template, data)

def about(request):
    teams = Team.objects.all()

    template = 'core/about.html'
    
    data = {
        'teams' : teams,
    }
    return render(request, template, data)

def services(request):
    template = 'core/services.html'
    return render(request, template)
