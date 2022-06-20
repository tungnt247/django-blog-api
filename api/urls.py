from django.urls import path
from . import views

user_list = views.UserAPIView.as_view({
    'get': 'list',
    'post': 'create'
})

user_detail = views.UserAPIView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

post_list = views.PostAPIView.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = views.PostAPIView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('users', user_list, name='user-list'),
    path('users/<int:pk>', user_detail, name='user-detail'),
    path('users/<int:user_id>/posts', post_list, name='post-list'),
    path('users/<int:user_id>/posts/<int:pk>', post_detail, name='post-detail')
]
