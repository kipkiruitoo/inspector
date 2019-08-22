from django.urls import path, include
from .views import InspectionViewSet, InsGradingViewSet, InsSummaryViewSet
from rest_framework import routers


router = routers.DefaultRouter()


router.register('inspections', InspectionViewSet)
router.register('insgrading', InsGradingViewSet)
router.register('summary', InsSummaryViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
