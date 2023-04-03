from rest_framework import serializers
from .models import Lecture


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'date', 'course_id', 'doctor_id')
