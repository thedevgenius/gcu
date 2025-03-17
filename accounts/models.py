from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from core.choices import *
from core.utils import get_hashid, generate_random_color, rename_image

from .managers import UserPasswordManager

hashids = get_hashid(saltname='user_id')
student_hash = get_hashid(saltname='student_id')
# Create your models here.
class User(AbstractUser):
    username_validator = RegexValidator(
        regex=r'^[\w@.+\-\/]+$',
        message='Username must be Alphanumeric',
    )
    username = models.CharField(max_length=150, unique=True, validators=[username_validator])
    email = models.EmailField(max_length=150, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    profile_color = models.CharField(max_length=10, default=generate_random_color, null=True, blank=True)
    profile_image = models.ImageField(upload_to=rename_image, null=True, blank=True)
    type = models.CharField(max_length=5, choices=USER_TYPE_CHOICES, default='ST')

    objects = UserPasswordManager()

    def __str__(self):
        return self.username

    def get_first_letter(self):
        return self.get_full_name()[0].upper() if self.first_name and self.last_name else 'A'
    
    def get_type(self):
        return dict(USER_TYPE_CHOICES)[self.type]
    
    def get_hash_id(self):
        return hashids.encode(self.id)
    


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    type = models.CharField(max_length=2, choices=ADDRESS_TYPE_CHOICES)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=3, choices=STATE_CHOICES)
    pincode = models.CharField(max_length=10)

    def get_address_type(self):
        return dict(ADDRESS_TYPE_CHOICES)[self.type]
    
    def get_state(self):
        return dict(STATE_CHOICES)[self.state]

    def __str__(self):
        return f'{self.user.username} - {self.get_address_type()}'

class Employee(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    department = models.CharField(max_length=5, choices=EMPLOYEE_DEPARTMENT_CHOICES)
    designation = models.CharField(max_length=150)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students')
    
    course = models.ForeignKey('academics.Course', on_delete=models.SET_NULL, null=True, blank=True)
    academic_year = models.ForeignKey('academics.AcademicYear', on_delete=models.SET_NULL, null=True, blank=True)
    semester = models.IntegerField(default=1)
    class_roll = models.PositiveIntegerField()
    uni_roll = models.PositiveIntegerField(unique=True, null=True, blank=True)
    reg_no = models.CharField(max_length=50, unique=True, null=True, blank=True)

    class_10 = models.JSONField(null=True, blank=True)
    class_12 = models.JSONField(null=True, blank=True)
    ug = models.JSONField(null=True, blank=True)
    pg = models.JSONField(null=True, blank=True)
    
    father_name = models.CharField(max_length=150, null=True, blank=True)
    father_phone = models.CharField(max_length=15, null=True, blank=True)
    father_profession = models.CharField(max_length=150, null=True, blank=True)
    father_income = models.BigIntegerField(null=True, blank=True)
    mother_name = models.CharField(max_length=150, null=True, blank=True)
    mother_phone = models.CharField(max_length=15, null=True, blank=True)
    mother_profession = models.CharField(max_length=150, null=True, blank=True)
    mother_income = models.BigIntegerField(null=True, blank=True)

    admission_date = models.DateTimeField()
    step = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username

    def get_hash_id(self):
        return student_hash.encode(self.id)
    

class Teacher(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    department = models.ForeignKey('academics.Department', on_delete=models.SET_NULL, null=True)
    designation = models.CharField(max_length=150)
    

    def __str__(self):
        return self.user.username
