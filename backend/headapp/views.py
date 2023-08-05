from django.shortcuts import render
from django.conf import settings
# Create your views here.

def index(request):
    template = 'home/index.html'
    return render(request, template)

def prices(request):
    template = 'prices/prices.html'
    return render(request, template)


def shop(request):
    template = 'shop/shop.html'
    return render(request, template)