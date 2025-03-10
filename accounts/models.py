from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from core.choices import *
from core.utils import get_hashid, generate_random_color, rename_image

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

    def __str__(self):
        return self.username
