from django.urls import path, include
from .views import UserViewSet, EmployeeViewSet
from rest_framework import routers


router = routers.DefaultRouter()


router.register('users', UserViewSet)
router.register('employees', EmployeeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
