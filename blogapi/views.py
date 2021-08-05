from rest_framework import serializers, viewsets
from rest_framework import authentication
from rest_framework.authentication import TokenAuthentication
from .serializers import BlogSerializer, UserSerializer, SponsorSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Blog, Sponsor

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated, )

class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    authentication_classes = (TokenAuthentication, )

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )