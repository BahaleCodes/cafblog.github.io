from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import BlogViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('blog', BlogViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]