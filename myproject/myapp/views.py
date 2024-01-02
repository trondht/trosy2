# create views using DRF's viewsets or generic views

from rest_framework import viewsets
from .models import MenstrualCycle, TrainingSession, GeneralHealthParameter
from .serializers import MenstrualCycleSerializer, TrainingSessionSerializer, GeneralHealthParameterSerializer

class MenstrualCycleViewSet(viewsets.ModelViewSet):
    queryset = MenstrualCycle.objects.all()
    serializer_class = MenstrualCycleSerializer

class TrainingSessionViewSet(viewsets.ModelViewSet):
    queryset = TrainingSession.objects.all()
    serializer_class = TrainingSessionSerializer

class GeneralHealthParameterViewSet(viewsets.ModelViewSet):
    queryset = GeneralHealthParameter.objects.all()
    serializer_class = GeneralHealthParameterSerializer
