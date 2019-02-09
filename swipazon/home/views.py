from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def display_homepage(request):
   return render(request, "homepage.html", {'today' : 'Friday'})
