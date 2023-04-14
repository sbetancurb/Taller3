from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains = searchTerm)
    else:
        movies = Movie.objects.all()

    return render(request,'home.html',{'searchTerm':searchTerm, 'movies':movies})

def teatro(request):
    teatros = Teatro.objects.all()
    return render(request,'teatros.html',{'teatros':teatros})