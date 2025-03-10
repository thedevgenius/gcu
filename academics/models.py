from django.db import models
from core.choices import COURSE_LEVEL_CHOICES

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=5)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    level = models.CharField(max_length=3, choices=COURSE_LEVEL_CHOICES)
    eligibility = models.TextField(null=True, blank=True)
    duration = models.IntegerField()
    max_students = models.IntegerField(default=30)

    def __str__(self):
        return self.name