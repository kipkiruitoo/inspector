from django.shortcuts import render
from rest_framework import viewsets
from .models import SysUser, Employee
from .serializers import UserSerializer, EmployeeSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = SysUser.objects.all()
    serializer_class = UserSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
