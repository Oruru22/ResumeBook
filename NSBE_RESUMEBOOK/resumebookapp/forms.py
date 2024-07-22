from django import forms
from .models import StudentInfo

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['Tnumber', 'LastName', 'FirstName', 'Email', 'Classification','Graduation_date', 'Major', 'Resume']
        
        