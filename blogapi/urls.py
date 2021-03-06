from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import BlogViewSet, UserViewSet, SponsorViewSet

router = routers.DefaultRouter()
router.register('blog', BlogViewSet)
router.register('users', UserViewSet)
router.register('sponsor', SponsorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]