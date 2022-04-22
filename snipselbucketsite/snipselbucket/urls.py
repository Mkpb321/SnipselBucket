from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.helloWorld, name='helloWorld'),
    path('hellotemplate', views.hello, name='hello'),
]

# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]