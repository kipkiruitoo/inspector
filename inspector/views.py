from django.shortcuts import render
from rest_framework import viewsets
from .models import Inspection, InsGrading, InsSummary

from .serializers import InspectionSerializer, InsGradingSerializer, InsSummarySerializer

# Create your views here.


class InspectionViewSet(viewsets.ModelViewSet):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer


class InsGradingViewSet(viewsets.ModelViewSet):
    queryset = InsGrading.objects.all()
    serializer_class = InsGradingSerializer


class InsSummaryViewSet(viewsets.ModelViewSet):
    queryset = InsSummary.objects.all()
    serializer_class = InsSummarySerializer
