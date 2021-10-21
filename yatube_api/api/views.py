from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.models import Comment, Follow, Group, Post, User
from .permissions import OwnerOrReadOnly, ReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer, UserSerializer)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self):
        obj = get_object_or_404(Group, id=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [OwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def get_object(self):
        obj = get_object_or_404(Post, id=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [OwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def get_object(self):
        obj = get_object_or_404(Comment, id=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post_pk'])
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username', 'user__username']

    def get_object(self):
        obj = get_object_or_404(Follow, id=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
