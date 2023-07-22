from django.http import HttpResponse
from django.shortcuts import render
from .models import posts

# Create your views here.
def index(request):
    tweets = posts.objects.all()
    return render(request, 'blog/index.html', {'tweets': tweets})
def create_post(request):
    author=request.POST.get('author','anonymus')
    content=request.POST.get('content')
    posts.objects.create(author_name=author,content=content)
    return index(request)