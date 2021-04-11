from django.urls import path
from .views import index,new,help,electronics,products

urlpatterns=[path("",products),path("products/",index),path("products/offers/",new),path("products/help/",help),path("products/Electronics/",electronics)]