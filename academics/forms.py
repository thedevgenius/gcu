from django import forms

from .models import Department

class DepartmentAddForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'e.g. Computer Science & Engineering', 'autofocus': 'true'}))
    code = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'e.g. CSE'}))

    class Meta:
        model = Department
        fields = '__all__'