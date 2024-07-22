from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse
from .models import StudentInfo
from .forms import StudentInfoForm
#from django.contrib.auth import authenticate, logout
import os


def index(request):
    if request.method == 'POST':
        form = StudentInfoForm(request.POST, request.FILES)
        if form.is_valid():
            Tnumber = form.cleaned_data['Tnumber']
            LastName = form.cleaned_data['LastName']
            FirstName = form.cleaned_data['FirstName']
            Email = form.cleaned_data['Email']
            Classification = form.cleaned_data['Classification']
            Graduation_date = form.cleaned_data['Graduation_date']
            Major = form.cleaned_data['Major']
            Resume = form.cleaned_data['Resume']
            
            student = StudentInfo(
                Tnumber=Tnumber,
                LastName=LastName,
                FirstName=FirstName,
                Email=Email,
                Classification=Classification,
                Graduation_date=Graduation_date,
                Major=Major,
                Resume=Resume.read()
            )
            form.save()
            
            return HttpResponse('Info Submitted.')
    else:
        form = StudentInfoForm()
    return render(request, 'resumebook.html', {'form': form})

def edit_form(request, tnumber):
    student = get_object_or_404(StudentInfo, Tnumber=tnumber)
    
    if request.method == 'POST':
        form= StudentInfoForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponse('Form entry updated successfully.')
    else:
        form = StudentInfoForm(instance=student)
    return render(request, 'resumebook.html', {'form': form})

def download_resume(request, student_id):
    student = StudentInfo.objects.get(Tnumber=student_id)
    
    response = HttpResponse(student.Resume, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="resume.pdf"'
    return response
