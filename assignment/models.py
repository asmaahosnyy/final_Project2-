from django.db import models


# Create your models here.

class Assignment(models.Model):
    grades = models.FloatField()
    description = models.TextField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} ({self.grades})"
