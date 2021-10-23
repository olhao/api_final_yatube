from django.urls import include, path
from rest_framework import routers
from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')
router.register(r'posts/(?P<post_pk>\d+)/comments',
                CommentViewSet, basename='comments')

VERSION_PARAM = 'v1'

urlpatterns = [
    path(f'{VERSION_PARAM}/', include(router.urls)),
    path(f'{VERSION_PARAM}/', include('djoser.urls')),
    path(f'{VERSION_PARAM}/', include('djoser.urls.jwt')),
]
