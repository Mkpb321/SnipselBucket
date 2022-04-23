from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView
from .models import Snipsel
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView

def helloWorld(request):
    return HttpResponse("Hello WorldBucket")

def hello(request):
    return render(request, 'snipselbucket/hello.html')

class SnipselHome(ListView):
    model = Snipsel
    template_name = 'snipselbucket/snipsel_home.html'

class SnipselCreate(CreateView):
    model = Snipsel
    template_name = 'snipselbucket/snipsel_create.html'
    fields = '__all__'
    success_url = reverse_lazy('snipsel_start')

class SnipselDetail(DetailView):
    model = Snipsel
    template_name = 'snipselbucket/snipsel_detail.html'