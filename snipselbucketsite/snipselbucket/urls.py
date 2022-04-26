from django.urls import path
from . import views
from .views import SnipselList, SnipselCreate, SnipselDetail, SnipselUpdate, SnipselDelete
from .views import CommentList, CommentCreate, CommentCreateSpecificSnipsel, CommentDetail, CommentUpdate, CommentDelete
from .views import DailySnipselsDetail

urlpatterns = [
    path('', views.index, name='index'),
    
    path('snipsel/', SnipselList.as_view(), name='snipsel_list'),
    path('snipsel/new/', SnipselCreate.as_view(), name='snipsel_create'),
    path('snipsel/<int:pk>/', SnipselDetail.as_view(), name='snipsel_detail'),
    path('snipsel/<int:pk>/update/', SnipselUpdate.as_view(), name='snipsel_update'),
    path('snipsel/<int:pk>/delete/', SnipselDelete.as_view(), name='snipsel_delete'),
    
    path('comment/', CommentList.as_view(), name='comment_list'),
    path('comment/new/', CommentCreate.as_view(), name='comment_create'),
    path('comment/new/<int:snipselpk>/', CommentCreateSpecificSnipsel.as_view(), name='comment_create_specific_snipsel'),
    path('comment/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),
    path('comment/<int:pk>/update/', CommentUpdate.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDelete.as_view(), name='comment_delete'),

    path('dailysnipsels/<int:pk>/', DailySnipselsDetail.as_view(), name='dailysnipsels_detail'),
]

# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

    # path('hello', views.helloWorld, name='helloWorld'),
    # path('hellotemplate', views.hello, name='hello'),