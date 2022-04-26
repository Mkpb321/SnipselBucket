from django.urls import path
from . import views
from .views import SnipselList, SnipselCreate, SnipselDetail, SnipselUpdate, SnipselDelete
from .views import CommentList, CommentCreate, CommentDetail, CommentUpdate, CommentDelete

urlpatterns = [
    path('', views.index, name='index'),
    
    path('snipsel/', SnipselList.as_view(), name='snipsel_list'),
    path('snipsel/new/', SnipselCreate.as_view(), name='snipsel_create'),
    path('snipsel/<int:pk>/', SnipselDetail.as_view(), name='snipsel_detail'),
    path('snipsel/<int:pk>/update/', SnipselUpdate.as_view(), name='snipsel_update'),
    path('snipsel/<int:pk>/delete/', SnipselDelete.as_view(), name='snipsel_delete'),
    
    path('comment/', CommentList.as_view(), name='comment_list'),
    path('comment/new/', CommentCreate.as_view(), name='comment_create'),
    path('comment/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),
    path('comment/<int:pk>/update/', CommentUpdate.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDelete.as_view(), name='comment_delete'),
]

# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

    # path('hello', views.helloWorld, name='helloWorld'),
    # path('hellotemplate', views.hello, name='hello'),