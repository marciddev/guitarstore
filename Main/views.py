from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
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
        "rentals": Rental.objects.all().order_by("-created_at")
    }
    return render(request, "Main/rentals.html", context)
def buynowrental(request, id):
    context = {
        "obj": Rental.objects.get(id=id)
    }
    return render(request, "Main/buynowrental.html", context)
def createrental(request):
    return render(request, "Main/rentalform.html")
def postrental(request):
    errors = Rental.objects.basic_validator(request.POST)
    if(len(errors) > 0):
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/rental/create')
    else:
        Rental.objects.create(price=request.POST['price'], image=request.POST['image'],duration=request.POST['duration'],brand=request.POST['brand'],model=request.POST['model'])
        return redirect("/rentals")
def repairs(request):
    return render(request, "Main/repairs.html")
def lessons(request):
    return render(request, "Main/lessons.html")
def checkout(request, id):
    context = {
        "id" : id
    }
    return render(request, "Main/checkout.html", context)