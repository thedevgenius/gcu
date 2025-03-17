from django.db import models
from core.choices import COURSE_LEVEL_CHOICES, DAY_CHOICES, COURSE_SYSTEM_CHOICES
from accounts.models import Student
from django.core.exceptions import ValidationError

# Create your models here.
class AcademicYear(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    current = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    admission_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.start_date.year} - {self.end_date.year}'
    
    def get_open(self):
        return 'Open' if self.is_open == True else 'Closed'

    # def get_total_student(self):
    #     students = Student.objects.filter(academic_year=self)
    #     return students.count()

class Department(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=5, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=5, unique=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    level = models.CharField(max_length=3, choices=COURSE_LEVEL_CHOICES)
    system = models.CharField(max_length=5, choices=COURSE_SYSTEM_CHOICES, default='SEM')
    duration = models.CharField(max_length=50)
    max_students = models.IntegerField(default=30)
    eligibility = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name

    def get_level(self):
        return dict(COURSE_LEVEL_CHOICES)[self.level]
    
    def get_total_student(self):
        students = Student.objects.filter(course=self)
        return students.count()
    
    

class Subject(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    semester = models.IntegerField()
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50)
    credit = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.code} {self.name}'
    

class Schedule(models.Model):
    day = models.CharField(max_length=5, choices=DAY_CHOICES)
    period = models.IntegerField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    semester = models.IntegerField()
    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey('accounts.Teacher', on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = [('day', 'period', 'course', 'semester'), ('day', 'period', 'teacher')]

    def __str__(self):
        return f'{self.course.code} - {self.day} - {self.period} - {self.subject}'