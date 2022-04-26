from re import S
from django.contrib import admin

from .models import Snipsel, Comment, DailySnipsels

admin.site.register(Snipsel)
admin.site.register(Comment)
admin.site.register(DailySnipsels)
