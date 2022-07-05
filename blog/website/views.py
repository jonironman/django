from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.fds
#fdf

def welcome(request): 
    return render(request, "website/welcome.html")


