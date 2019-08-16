from django.shortcuts import render
from rest_framework import viewsets
from .models import SysUser
from .serializers import UserSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = SysUser.objects.all()
    serializer_class = UserSerializer
