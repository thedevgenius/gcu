from django import forms

class FeeAddForm(forms.Form):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'class':'input'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    breakdown = forms.JSONField(widget=forms.HiddenInput())