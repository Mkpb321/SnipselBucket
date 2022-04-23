from django.urls import path
from . import views
from .views import SnipselHome
from .views import SnipselCreate
from .views import SnipselDetail

urlpatterns = [
    path('hello', views.helloWorld, name='helloWorld'),
    path('hellotemplate', views.hello, name='hello'),
    path('', SnipselHome.as_view(), name='snipsel_start'),
    path('neu/', SnipselCreate.as_view(), name='neue_snipsel'),
    path('<int:pk>/', SnipselDetail.as_view(), name='snipsel_detail'),
]

# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]