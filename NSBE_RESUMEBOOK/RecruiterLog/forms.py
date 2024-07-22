from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Recruiter
from homepage.models import CustomUser

class RecruiterRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Recruiter
        fields = ['first_name', 'last_name', 'email', 'company', 'password']
        
    def save(self, commit=True):
        recruiter = super().save(commit=False)
        recruiter.is_recruiter = True
        
        if commit:
            recruiter.save()
        return recruiter
        
# class RecruiterLoginForm(AuthenticationForm):
#     email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Email")
#     #password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Password")
    
#     class Meta:
#         model = Recruiter
#         fields = ['email', 'password']

class RecruiterLoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your password'})
    )
    
    