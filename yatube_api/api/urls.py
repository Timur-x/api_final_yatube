from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'groups', GroupViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
v1_router.register(r'follow', FollowViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    # Djoser создаст набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    path('v1/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('v1/', include('djoser.urls.jwt')),
]
