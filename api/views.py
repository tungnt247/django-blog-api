from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from .serializers import UserSerializer, PostSerializer
from .models import User, Post
from .mixin import ViewSetMixin


class UserAPIView(viewsets.GenericViewSet, ViewSetMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        users = User.objects.all()
        results = []
        for user in users:
            posts = user.post_set.values_list('title', flat=True)
            data = {
                'name': user.name,
                'email': user.email,
                'posts': posts,
                'created_at': user.created_at,
                'updated_at': user.updated_at
            }
            results.append(data)
        return Response(results)


class PostAPIView(viewsets.GenericViewSet, ViewSetMixin):
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        user = self.__load_user(kwargs['user_id'])
        if not user:
            return Response('user do not existed!', status=status.HTTP_404_NOT_FOUND)

        request.data['user'] = kwargs['user_id']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        user = self.__load_user(self.kwargs['user_id'])
        queryset = Post.objects.filter(user=user)
        return queryset

    def __load_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except:
            return None
