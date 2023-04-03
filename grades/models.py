from django.db import models
from courses.models import Course
from users.models import Student
# Create your models here.


class Grades(models.Model):
    score = models.FloatField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.score)


