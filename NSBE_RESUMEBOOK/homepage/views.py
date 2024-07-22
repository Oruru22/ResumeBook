from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm
from resumebookapp.forms import StudentInfoForm
from .forms import LoginForm
from .models import CustomUser
from .backends import EmailBackend
from django.contrib import messages
from resumebookapp.models import StudentInfo

def home(request):
    #check if user already logged in
    # if request.user.is_authenticated:
    #     form = StudentInfoForm()
    #     return render(request, 'resumebook.html', {'form': form})

    #if not logged in, give option to sign up or log in
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            #to create a new user
            user = CustomUser.objects.create_user(email=email, password=password)
            user.save()
        
            #log in the user
            user= authenticate(request, email=email, password=password)
            login(request, user)
            return redirect('resumebookapp:index')
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            #authenticate user
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                
                #Check if the user has previously filled the form
                try:
                    student_info = StudentInfo.objects.get(Email=email)
                    #if user has previously filled the form, allow them to edit it
                    return redirect('resumebookapp:edit_form', student_info.Tnumber)
                except StudentInfo.DoesNotExist:
                    return redirect('resumebookapp:index')
            else: 
                messages.error(request, 'Invalid login credential. Please try again.')
        else:
            messages.error(request, 'Invalid form data. Please check the form fields.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('homepage:home')
'''''''''''
@login_required
def edit_info(request):
    user = request.user
    if request.method == 'POST':
        form = StudentInfoForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            user.has_submitted_info = True
            user.save()
            return redirect('homepage:home')
    else:
        if user.has_submitted_info:
            form = StudentInfoForm(instance=user)
        else:
            form = StudentInfoForm()
    return render(request, 'edit_info.html', {'form':form})

'''''''''''''''

#Error check.
#current error: TypeError:cannot pickly 'module' object
# check later
#for some reason, the error dissapeared after i restarted the server
# at the moment, not able to access homepage


#loginform works
# sigupform works
# studentinfo form works, successfully able to accept and store resumes
# 
# 
# next up
# add a logout functionality in the student info page
# logout should take them back to homepage
# 
# well shit, i guess i have to hardcode the html template and somehow connect 
# it to the corresponding function that renders the template
# 
# 
# nevermind, it works now, had to create an instance of the form and rendered 
# it in the home function
#.
            


    

