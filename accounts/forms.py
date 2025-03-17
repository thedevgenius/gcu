from django import forms
from django.contrib.auth.forms import AuthenticationForm
from core.choices import GENDER_CHOICES, BLOOD_GROUP_CHOICES, STATE_CHOICES, USER_TYPE_CHOICES
from academics.models import Course, Department

from .choices import BOARD_CHOICES, YEAR_CHOICES

class SignInForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class UserAddForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'input', 'placeholder' : 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'Phone'}))
    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES, attrs={'class':'select'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'class':'input'}))
    blood_group = forms.CharField(widget=forms.Select(choices=BLOOD_GROUP_CHOICES, attrs={'class':'select'}))

class StudentAddForm(UserAddForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label='Select Course', widget=forms.Select(attrs={'class':'select'}))
    

class AcademicForm(forms.Form):
    class_10_board = forms.IntegerField(widget=forms.Select(choices=BOARD_CHOICES, attrs={'class':'select'}))
    class_10_year = forms.IntegerField(label='Passing Year', widget=forms.Select(choices=YEAR_CHOICES, attrs={'class':'select'}))
    class_10_fm = forms.IntegerField(label='Full Marks', required=True, widget=forms.NumberInput(attrs={'class':'select'}))
    class_10_om = forms.IntegerField(label='Obtained Mark', required=True, widget=forms.NumberInput(attrs={'class':'input'}))

    class_12_board = forms.IntegerField(widget=forms.Select(choices=BOARD_CHOICES, attrs={'class':'select'}))
    class_12_year = forms.IntegerField(label='Passing Year', widget=forms.Select(choices=YEAR_CHOICES, attrs={'class':'select'}))
    class_12_fm = forms.IntegerField(label='Full Marks', required=True, widget=forms.NumberInput(attrs={'class':'select'}))
    class_12_om = forms.IntegerField(label='Obtained Mark', required=True, widget=forms.NumberInput(attrs={'class':'input'}))

class AddressForm(forms.Form):
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Address'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'City'}))
    state = forms.CharField(widget=forms.Select(choices=STATE_CHOICES, attrs={'class':'select'}))
    pincode = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'PIN Code'}))

class TeaheerAddForm(UserAddForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label='-- Select Department --', widget=forms.Select(attrs={'class':'select'}))
    designation = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
