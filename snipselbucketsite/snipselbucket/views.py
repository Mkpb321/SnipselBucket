from django.shortcuts import render

from django.http import HttpResponse

def helloWorld(request):
    return HttpResponse("Hello World")

def hello(request):
    return render(request, 'snipselbucket/hello.html')