from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={
        'placeholder': 'Enter your name'
    }))
    phone = forms.CharField(label='',widget=forms.TextInput(attrs={
        'placeholder': 'Enter your phone number'
    }))
    email = forms.CharField(label='',widget=forms.TextInput(attrs={
        'placeholder': 'Enter your email address'
    }))
    designation = forms.CharField(label='',widget=forms.TextInput(attrs={
        'placeholder': 'Enter your desination'
    }))

    class Meta:
        model = Employee
        fields = ('name', 'email', 'phone', 'designation')
