from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    tweets = posts.objects.all()
    return render(request, '', {'tweets': tweets})
