from django.urls import path
from . import views

app_name = 'RecruiterLog'

urlpatterns =[
    path('registration/', views.recruiter_registration, name='recruiter_registration'),
    path('recruiterlogin/', views.recruiter_login, name='recruiter_login' ),
    path('student-info/', views.student_info, name='student_info'),
    path('download-resume/<str:tnumber>/', views.download_student_resume, name='download_student_resume'),
    path('recruiterlogout/', views.recruiter_logout, name='recruiter_logout'),
]



