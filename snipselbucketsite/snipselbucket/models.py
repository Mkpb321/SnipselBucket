from django.db import models
from django.urls import reverse

class Snipsel(models.Model):
    text = models.TextField()
    source = models.TextField()
    weight = models.IntegerField(choices=list(zip(range(1, 101), range(1, 101))))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.text[:50] + "... (" + self.source + ")"

    def get_absolute_url(self): # https://youtu.be/dv1Sm2Rlyao
        return reverse('snipsel_detail', args=[str(self.id)])

class Comment(models.Model):
    text = models.TextField()
    snipsel = models.ForeignKey(Snipsel, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.text[:50] + "... (" + self.snipsel.text[:10] + ")"

    def get_absolute_url(self): # https://youtu.be/dv1Sm2Rlyao
        return reverse('comment_detail', args=[str(self.id)])

class DailySnipsels(models.Model):
    snipsels = models.ManyToManyField(Snipsel)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        name = ""
        for snipsel in self.snipsels.all():
            name += str(snipsel) + " "
        return name