from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.views.generic import ListView
from .models import DailySnipsels, Snipsel, Comment
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
import os
import json
import random


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

class CommentCreateSpecificSnipsel(CreateView):
    model = Comment
    template_name = 'snipselbucket/comment_create_specific_snipsel.html'
    fields = ['text']
    success_url = reverse_lazy('index')

    # def get_success_url(self):
    #             return reverse('comment_list', args=[1])

    def get_context_data(self, **kwargs):
        pk = self.kwargs['snipselpk']
        context = super(CommentCreateSpecificSnipsel, self).get_context_data(**kwargs)
        context.update({'snipsel': Snipsel.objects.get(pk=pk),})
        return context

    def form_valid(self, form):
        pk = self.kwargs['snipselpk']
        form.instance.snipsel = Snipsel.objects.get(pk=pk)
        return super(CommentCreateSpecificSnipsel, self).form_valid(form)

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


## DailySnipsels ##

class DailySnipselsDetail(DetailView):
    model = DailySnipsels
    template_name = 'snipselbucket/dailysnipsels_detail.html'

def dailySnipsels(request):
    return render(request, 'snipselbucket/dailysnipsels.html')

def newRandomDailySnipsels(request):
    snipsel_pk_list = []
    for snipsel in Snipsel.objects.all():
        snipsel_pk_list.append(snipsel.pk)
    random_snipsel_pk_list = random.sample(snipsel_pk_list, 3)
    randomDailySnipsels = DailySnipsels()
    randomDailySnipsels.save()
    for pk in random_snipsel_pk_list:
        randomDailySnipsels.snipsels.add(pk)
    return HttpResponse(random_snipsel_pk_list)

def newestDailySnipsels(request):
    snipsel = DailySnipsels.objects.all().order_by("created_at").reverse().first()
    return redirect('dailysnipsels_detail', snipsel.pk)

## Kindle ##

def kindle(request):
    log = ""
    with open("kindle/input.json", "r", encoding='utf-8') as f:
        data = json.load(f)

    for highlite in data["highlights"]:
        if not Snipsel.objects.filter(text=highlite["text"]):
            snipsel_text = (highlite["text"])
            snipsel_source = (str(data["authors"]) + ", " + data["title"])
            snipsel_weight = 100
            snipsel = Snipsel.objects.create(text=snipsel_text, source=snipsel_source, weight=snipsel_weight)
            log += str(snipsel) + '<br>'

            if highlite["note"]:
                comment_text = str(highlite["note"])
                comment_snipsel = snipsel
                comment = Comment.objects.create(text=comment_text, snipsel=comment_snipsel)
                log += str(comment) + '<br>'
        else:
            log += 'SNIPSEL ALREADY EXISTS<br>'

    log += str(data)
    return HttpResponse(log)

# def helloWorld(request):
#     return HttpResponse(os.name)

# def inde(request):
#     return render(request, 'snipselbucket/hello.html')