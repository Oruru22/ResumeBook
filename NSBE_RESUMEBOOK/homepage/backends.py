from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        
    def get_user(self,user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

'''''''''
User = get_user_model

class EmailBackEnd(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        if email is None or password is None:
            return
        try: 
            user = User.objects.get(Q(email__iexact=email) | Q(username__iexact=email))
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return
    
    def get_user(self,user_id):
        try:
            return User.Objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
'''''''''
