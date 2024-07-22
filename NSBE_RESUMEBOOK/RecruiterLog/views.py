from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
#from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import RecruiterRegistrationForm, RecruiterLoginForm
from resumebookapp.models import StudentInfo
from django.http import HttpResponse, FileResponse
from resumebookapp.forms import StudentInfoForm
from .backends import RecruiterBackend
from django.urls import reverse
from .models import Recruiter
from homepage.models import CustomUser
from django.contrib import messages

# def recruiter_registration(request):
#     if request.method == 'POST':
#         print("first if")
#         form = RecruiterRegistrationForm(request.POST)
#         if form.is_valid():
#             recruiter = form.save()
#             print("second if")
#             #authenticate the recruiter using the custom backend
#             #recruiter.backend = 'RecruiterLog.backends.RecruiterBackend'
#             authenticated_recruiter = authenticate(
#                 request, email=form.cleaned_data['email'], password=form.cleaned_data['password']
#             )
#             print(authenticated_recruiter)
#             if authenticated_recruiter:
#                 print("third if")
#                 login(request, authenticated_recruiter)
#                 return redirect('RecruiterLog:student_info')
#                 #return redirect('student_info.html')
#                 #return render(request, 'student_info.html')
#     else:
#         form = RecruiterRegistrationForm()
    
#     return render(request, 'recruiter_registration.html', {'form': form})

#use the same format for homepage:signp and use it for RecruiterLog:recruiter_registration
#compare difference in results
def recruiter_registration(request):
    if request.method == 'POST':
        form = RecruiterRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            #to create a new user
            recruiter_user = CustomUser.objects.create_user(email=email, password=password)
            recruiter_user.backend = 'RecruiterLog.backends.RecruiterBackend'
            recruiter_user.save()
            
            #log the user in
            recruiter_user = authenticate(request, email=email, password=password)
            login(request, recruiter_user)
            print(recruiter_user)
            return redirect('RecruiterLog:student_info')
    else:
        form = RecruiterRegistrationForm()
            
    return render(request, 'recruiter_registration.html', {'form': form})
    
@login_required
def student_info(request):
    #Fetch student info and display in a tabular format
    students = StudentInfo.objects.all()#fetch all student info
    context = {
        'students': students
    }
    return render(request, 'student_info.html', context)

@login_required
def download_student_resume(request, tnumber):
    student = get_object_or_404(StudentInfo, Tnumber=tnumber)
    
    response = HttpResponse(student.Resume, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="resume.pdf"'
    return response

# def recruiter_login(request):
#     if request.method == 'POST':
#         print("wow")
#         form = RecuiterLoginForm(request, data=request.POST)
#         print(form)
#         if form.is_valid():
#             print("second")
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=email, password=password)
#             print("sucess")
#             if user is not None and user.is_recruiter:
#                 print("success again")
#                 login(request, user)
#                 return redirect('RecruiterLog:student_info')
#     else:
#         form = RecuiterLoginForm()
#     return render(request, 'recruiter_login.html', {'form': form})

def recruiter_login(request):
    if request.method == 'POST':
        form = RecruiterLoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            recruiter_user = authenticate(request, username=email, password=password)
            
            if recruiter_user is not None:
                login(request, recruiter_user)
                return redirect('RecruiterLog:student_info')
            else:
                messages.error(request, 'Invalid login credential. Please try again.')
        else:
            messages.error(request, 'Invalid form data. Please check the form fields.')
    else:
        form = RecruiterLoginForm()
    return render(request, 'recruiter_login.html', {'form':form}) 
            
def recruiter_logout(request):
    logout(request)
    return redirect('homepage:home')