from django import forms

from core.choices import COURSE_LEVEL_CHOICES, SEMESTER_CHOICE
from .models import Department, Course, Subject

class DepartmentAddForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'e.g. Computer Science & Engineering', 'autofocus': 'true'}))
    code = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'e.g. CSE'}))
    is_academic = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    class Meta:
        model = Department
        fields = '__all__'

class CourseAddForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'e.g. B. Tech', 'autofocus': 'true'}))
    code = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'e.g. BTCS'}))
    level = forms.CharField(widget=forms.Select(choices=[('', '--- Select Course Level --')] + COURSE_LEVEL_CHOICES, attrs={'class' : 'select'}))
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label='-- Select Department --', widget=forms.Select(attrs={'class' : 'select'}))
    duration = forms.IntegerField(label='Duration in Years', widget=forms.NumberInput(attrs={'class' : 'input', 'placeholder' : 'e.g. 4'}))
    max_students = forms.IntegerField(label='Seat Capacity', widget=forms.NumberInput(attrs={'class' : 'input', 'placeholder' : 'e.g. 60'}))
    eligibility = forms.CharField(label='Minimum Eligibility', required=False, widget=forms.Textarea(attrs={'class' : 'textarea', 'placeholder' : 'Minimum eligibility criteria for the course'}))

    class Meta:
        model = Course
        fields = '__all__'


class SubjectAddForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'Subject Name', 'autofocus': 'true'}))
    code = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'Subject Code'}))
    credit = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'input', 'placeholder' : 'Subject Credit'}))