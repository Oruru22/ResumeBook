from django.urls import path
from . import views

app_name = 'resumebookapp'

urlpatterns = [
    path('resumebook/', views.index, name='index'),
    #path('submit/', views.submit_data, name='submit_data'),
    path('resumebook/download/<int:student_id>/', views.download_resume, name='download_resume'),
    path('edit-form/<str:tnumber>/', views.edit_form, name='edit_form'),
]