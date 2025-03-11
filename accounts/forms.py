from django import forms
from django.contrib.auth.forms import AuthenticationForm
from core.choices import GENDER_CHOICES, BLOOD_GROUP_CHOICES
from academics.models import Course

class SignInForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class StudentAddForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'Last Name'}))
    course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label='Select Course', widget=forms.Select(attrs={'class':'select'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'input', 'placeholder' : 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'Phone'}))
    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES, attrs={'class':'select'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'class':'input'}))
    blood_group = forms.CharField(widget=forms.Select(choices=BLOOD_GROUP_CHOICES, attrs={'class':'select'}))

# class AcademicForm(forms.Form):
#     class_10_board = 