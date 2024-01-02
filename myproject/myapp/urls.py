# Set up URLs for the backend API

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenstrualCycleViewSet, TrainingSessionViewSet, GeneralHealthParameterViewSet

router = DefaultRouter()
router.register(r'menstrualcycles', MenstrualCycleViewSet)
router.register(r'trainingsessions', TrainingSessionViewSet)
router.register(r'generalhealthparameters', GeneralHealthParameterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
