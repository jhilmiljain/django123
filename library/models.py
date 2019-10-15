from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
# Create your models here.
class UserManager(BaseUserManager):
     def create_user(self, email, fname, lname, password=None, is_staff=False, is_admin=False, is_active=True):
        if not email:
            raise ValueError("users must sign in")
        if not password:
            raise ValueError("users must have a password")    
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.setpassword(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using= self._db)
        return user_obj

     def create staff_user(self, email, password=None):
         user = self.create_user(
                email,
                password=password,
                is_staff=True

            )
         return user    

class User(AbstractBaseUser):
    email   = models.EmailField(max_length=255, unique= True)
    fname   = models.CharField(max_length=255, blank=True, null=True)
    lname   = models.CharField(max_length=255, blank=True, null=True)
    active  = models.BooleanField(default= True)
    staff   = models.BooleanField(default= False)
    admin   = models.BooleanField(default= False)
    timestamp = models.DateTimeField(auto_now_add= True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELD = []

    objects  = 'UserManager'

    def __str__(self):
        return 

    def get_fname(self):
        return    
    
    def get_lname(self):
        return 

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
    
s tEmail(models.Model):
    email     = models.EmailField()
    active    = models.BooleanField(default= True)
    update    = models.DateTimeField(auto_now= True)
    timestamp = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.email
