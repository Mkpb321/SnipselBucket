from django.urls import path
from . import views
from .views import SnipselList
from .views import SnipselCreate
from .views import SnipselDetail
from .views import SnipselUpdate
from .views import SnipselDelete

urlpatterns = [
    path('', views.index, name='index'),
    path('snipsel/', SnipselList.as_view(), name='snipsel_list'),
    path('new/', SnipselCreate.as_view(), name='snipsel_create'),
    path('<int:pk>/', SnipselDetail.as_view(), name='snipsel_detail'),
    path('<int:pk>/update/', SnipselUpdate.as_view(), name='snipsel_update'),
    path('<int:pk>/delete/', SnipselDelete.as_view(), name='snipsel_delete'),
]

# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

    # path('hello', views.helloWorld, name='helloWorld'),
    # path('hellotemplate', views.hello, name='hello'),