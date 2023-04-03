from django.db import models


# Create your models here.

class Timetable(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.start_time} - {self.end_time} ({self.location})"
