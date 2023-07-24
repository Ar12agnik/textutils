from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
def index(request):
    prods=Product.objects.all()
    return render(request,'shop\index.html',{"products":prods})
def about(request):
    return render(request,'shop\\about.html')
def contact(request):
    return HttpResponse("we are at contact")
def tracker(request):
    return HttpResponse("we are at tracker")
def search(request):
    return HttpResponse("we are at search")
def prodView(request):
    return HttpResponse("we are at product view")
def checkout(request):
    return HttpResponse("we are at checkout")
