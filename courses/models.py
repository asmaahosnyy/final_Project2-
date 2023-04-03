from django.db import models
from users.models import Student


# Create your models here.

class Course(models.Model):
    course_description = models.TextField()
    course_name = models.CharField(max_length=255)
    course_credit_hour = models.PositiveIntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name
