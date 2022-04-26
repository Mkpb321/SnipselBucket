from django.db import models
from django.urls import reverse

class Snipsel(models.Model):
    text = models.TextField()
    source = models.TextField()
    weight = models.IntegerField(choices=list(zip(range(1, 101), range(1, 101))))
        
    def __str__(self):
        return self.text[:10] + "... (" + self.source + ")"

    def get_absolute_url(self): # https://youtu.be/dv1Sm2Rlyao
        return reverse('snipsel_detail', args=[str(self.id)])

class Comment(models.Model):
    text = models.TextField()
    snipsel = models.ForeignKey(Snipsel, related_name="comments", on_delete=models.CASCADE)
        
    def __str__(self):
        return self.text[:10] + "... (" + self.snipsel.text[:10] + ")"