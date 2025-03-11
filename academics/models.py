from django.db import models
from core.choices import COURSE_LEVEL_CHOICES

# Create your models here.
class AcademicYear(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    is_open = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.start_date.year} - {self.end_date.year}'


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
    duration = models.IntegerField()
    max_students = models.IntegerField(default=30)
    eligibility = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_level(self):
        return dict(COURSE_LEVEL_CHOICES)[self.level]