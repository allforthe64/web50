from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#index route
def index(request):
    return render(request, "hello/index.html")

#greet route
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name":name.capitalize()
    })