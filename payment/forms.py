from django import forms

from core.choices import FEE_TYPE_CHOICES

class FeeAddForm(forms.Form):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'class':'input'}))
    type = forms.CharField(widget=forms.Select(choices=FEE_TYPE_CHOICES, attrs={'class':'select'}))
    breakdown = forms.JSONField(widget=forms.HiddenInput())