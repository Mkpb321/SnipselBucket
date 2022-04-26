from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView
from .models import Snipsel, Comment
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
import os

def index(request):
    return render(request, 'snipselbucket/index.html')


## Snipsel ##

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


## Comment ##

class CommentList(ListView):
    model = Comment
    template_name = 'snipselbucket/comment_list.html'

class CommentCreate(CreateView):
    model = Comment
    template_name = 'snipselbucket/comment_create.html'
    fields = '__all__'
    success_url = reverse_lazy('comment_list')

class CommentDetail(DetailView):
    model = Comment
    template_name = 'snipselbucket/comment_detail.html'

class CommentUpdate(UpdateView):
    model = Comment
    template_name = 'snipselbucket/comment_update.html'
    fields = '__all__'

class CommentDelete(DeleteView):
    model = Comment
    template_name = 'snipselbucket/comment_delete.html'
    success_url = reverse_lazy('comment_list')

# def helloWorld(request):
#     return HttpResponse(os.name)

# def inde(request):
#     return render(request, 'snipselbucket/hello.html')