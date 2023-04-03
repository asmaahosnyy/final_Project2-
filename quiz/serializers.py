from rest_framework import serializers
from .models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'exam_type', 'exam_time')
