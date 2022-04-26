from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView
from .models import Snipsel
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
import os

def index(request):
    return render(request, 'snipselbucket/index.html')

class SnipselList(ListView):
    model = Snipsel
    template_name = 'snipselbucket/snipsel_list.html'

class SnipselCreate(CreateView):
    model = Snipsel
    template_name = 'snipselbucket/snipsel_create.html'
    fields = '__all__'
    success_url = reverse_lazy('snipsel_list')

class SnipselDetail(DetailView):
    model = Snipsel
    template_name = 'snipselbucket/snipsel_detail.html'

class SnipselUpdate(UpdateView):
    model = Snipsel
    template_name = 'snipselbucket/snipsel_update.html'
    fields = '__all__'

class SnipselDelete(DeleteView):
    model = Snipsel
    template_name = 'snipselbucket/snipsel_delete.html'
    success_url = reverse_lazy('snipsel_list')

# def helloWorld(request):
#     return HttpResponse(os.name)

# def inde(request):
#     return render(request, 'snipselbucket/hello.html')