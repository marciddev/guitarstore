from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^sales$', views.sales),
    path('buynow/<int:id>', views.buynow),
    url(r'^rentals$', views.rentals)
]