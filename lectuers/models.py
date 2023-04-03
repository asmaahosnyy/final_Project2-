from django.db import models
from users.models import Doctor
from courses.models import Course


# Create your models here.
class Lecture(models.Model):
    date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.course.title} ({self.doctor.first_name} {self.doctor.last_name})"
