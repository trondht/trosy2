# Define serializers to convert model instances to JSON and vice versa

from rest_framework import serializers
from .models import MenstrualCycle, TrainingSession, GeneralHealthParameter

class MenstrualCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenstrualCycle
        fields = '__all__'

class TrainingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSession
        fields = '__all__'

class GeneralHealthParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralHealthParameter
        fields = '__all__'

