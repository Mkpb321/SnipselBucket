from django.db import models
from django.urls import reverse

class Snipsel(models.Model):
    text = models.TextField()
    number = models.IntegerField()
        
    def __str__(self):
        return "Ich bin Nr.:" + str(self.number)

    def get_absolute_url(self): # https://youtu.be/dv1Sm2Rlyao
        return reverse('snipsel_detail', args=[str(self.id)])