from django.db import models

# Create your models here.
class StudentInfo(models.Model):
   #fields for StudentInfo model
   Tnumber = models.CharField(max_length=9, primary_key=True)
   LastName = models.CharField(max_length=50)
   FirstName = models.CharField(max_length=50)
   Email= models.EmailField()
   Classification = models.CharField(max_length=50)
   Graduation_date = models.CharField(max_length=50)
   Major = models.CharField(max_length=50)
   Resume = models.FileField(upload_to='resumes/')
   
   def __str__(self):
       return f"{self.FirstName} {self.LastName}"


