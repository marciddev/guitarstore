from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
def index(request):
    return render(request, "Main/dash.html")
def sales(request):
    context = {
        "sales": Guitar.objects.all()
    }
    return render(request, "Main/sales.html", context)
def buynow(request, id):
    context = {
        "obj": Guitar.objects.get(id=id)
    }
    return render(request, "Main/buynow.html", context)
def rentals(request):
    context = {
        "rentals": Rental.objects.all()
    }
    return render(request, "Main/rentals.html", context)