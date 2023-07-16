#made by Agnik
from django.http import HttpResponse
def index(requests):
    return HttpResponse("<h1>hello</h1> <a href='https://github.com/ar12agnik'>github</a> <a href='https://www.youtube.com/'>youtube</a>")