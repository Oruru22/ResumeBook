from django.db import models
from resumebookapp.models import StudentInfo
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission, Group
from homepage.models import CustomUser

class RecruiterManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)       

class Recruiter(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    company = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    is_recruiter = models.BooleanField(default=True)
    
    groups = models.ManyToManyField(Group, blank=True, related_name='recruiters')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='recruiters')
    
    objects = RecruiterManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'company']
    
    def __str__(self):
        return self.email
    
# class StudentInfoAccess(models.Model):
#     recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
#     student_info = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)