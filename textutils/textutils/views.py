#i have created this file -Agnik
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    
    return render(request,'index.html')
    #return HttpResponse("Home <a href='/removepunc'>removepunc</a> <a href='/capitalizefirst'>capfirst</a> <a href='/newlineremove'>newlineremove</a><a href='/spaceremove'>spaceremove</a><a href='/charcount'>charcount</a>")

def analyze(request):
    #get the text
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print(removepunc)
    #analize the text
    print(djtext)
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed=''
    if removepunc=="on":
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'pourpose':'remove puncuation','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    else:
        return HttpResponse("ERROR")

'''def capfirst(request):
    return HttpResponse("capitalize first <a href='..'>home</a>")

def newlineremove(request):
    return HttpResponse("capitalize first <a href='..'>home</a>")


def spaceremove(request):
    return HttpResponse("space remover <a href='..'>home</a>")

def charcount(request):
    return HttpResponse("charcount <a href='..'>home</a>")
    '''
