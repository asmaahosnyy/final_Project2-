from django.db import models


# Create your models here.

class Quiz(models.Model):
    exam_type = models.CharField(max_length=100)
    exam_time = models.DateTimeField()

    def __str__(self):
        return f"{self.exam_type} ({self.exam_time})"
