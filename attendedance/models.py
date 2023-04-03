from django.db import models


# Create your models here.

class Attendance(models.Model):
    lecture_date = models.DateField()

    def __str__(self):
        return f"{self.lecture_date}"
