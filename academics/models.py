from django.db import models
from core.choices import COURSE_LEVEL_CHOICES, SEMESTER_CHOICE, GRADE_NAME_CHOICES
from accounts.models import Student
from django.core.exceptions import ValidationError

# Create your models here.
class AcademicYear(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    is_open = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.start_date.year} - {self.end_date.year}'
    
    def get_open(self):
        return 'Open' if self.is_open == True else 'Closed'

    def get_student_count(self):
        students = Student.objects.filter(academic_year=self)
        return students.count()

class Department(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=5)
    is_academic = models.BooleanField(default=False)

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
    
    def get_student_count(self):
        students = Student.objects.filter(course=self)
        return students.count()
    
def is_even(num):
    return True if num%2 == 0 else False

    
class Grade(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    number = models.IntegerField(choices=SEMESTER_CHOICE)
    name = models.CharField(max_length=5, choices=GRADE_NAME_CHOICES)
    status = models.BooleanField(default=False)

    class Meta:
        unique_together = ['course', 'number']
    
    def __str__(self):
        return f'{self.course.code} {self.name} {self.number}'
    
    # def clean(self):
    #     if is_even(self.number) and Grade.objects.filter(course=self.course, number__in=[1, 3, 5, 7], status=True).exists():
    #         raise ValidationError("You can't activate both Odd and Even Semesters")
    #     super().clean()
    
    # def save(self, *args, **kwargs):
    #     self.clean()
    #     return super().save(*args, **kwargs)
    


class Subject(models.Model):
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50)
    credit = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.code} {self.name}'