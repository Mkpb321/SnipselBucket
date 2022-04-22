from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('snipselbucket.urls')),
]


# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('polls/', include('polls.urls')),
#     path('admin/', admin.site.urls),
# ]