from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Offer,Help,Home


def index(request):
    products=Product.objects.all()
    return render(request,"index.html",{"products":products})


def new(request):
    offers=Offer.objects.all()
    return render(request,"offer.html",{"offers":offers})


def help(request):
    return render(request,'help.html')


def electronics(request):
    return render(request,'Electronics.html')


def products(request):
    home=Home.objects.all()
    return render(request,'home.html',{"home":home})