from re import S
from django.contrib import admin

from .models import Snipsel, Comment

admin.site.register(Snipsel)
admin.site.register(Comment)
