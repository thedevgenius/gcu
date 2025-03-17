from django import forms

from core.choices import COURSE_LEVEL_CHOICES, SEMESTER_CHOICE, COURSE_SYSTEM_CHOICES
from .models import Department, Course

class DepartmentAddForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'e.g. Computer Science & Engineering', 'autofocus': 'true'}))
    code = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'e.g. CSE'}))

    class Meta:
        model = Department
        fields = ['name', 'code']

class CourseAddForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'e.g. B. Tech', 'autofocus': 'true'}))
    code = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'e.g. BTCS'}))
    level = forms.CharField(widget=forms.Select(choices=[('', '--- Select Course Level --')] + COURSE_LEVEL_CHOICES, attrs={'class' : 'select'}))
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label='-- Select Department --', widget=forms.Select(attrs={'class' : 'select'}))
    duration = forms.CharField(label='Duration in Years', widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'e.g. 4 Year'}))
    max_students = forms.IntegerField(label='Seat Capacity', widget=forms.NumberInput(attrs={'class' : 'input', 'placeholder' : 'e.g. 60'}))
    eligibility = forms.CharField(label='Minimum Eligibility', required=False, widget=forms.Textarea(attrs={'class' : 'textarea', 'placeholder' : 'Minimum eligibility criteria for the course'}))
    system = forms.CharField(widget=forms.Select(choices=COURSE_SYSTEM_CHOICES, attrs={'class':'select'}))

    class Meta:
        model = Course
        fields = '__all__'