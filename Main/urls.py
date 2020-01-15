from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^sales$', views.sales),
    path('buynow/<int:id>', views.buynow),
    path('buynow/rental/<int:id>', views.buynowrental),
    url(r'^rentals$', views.rentals),
    url(r'^rental/create$', views.createrental),
    url(r'^rental/redirect$', views.postrental),
    url(r'^repairs$', views.repairs),
    url(r'^lessons$', views.lessons),
    path('checkout/<int:id>', views.checkout)
]