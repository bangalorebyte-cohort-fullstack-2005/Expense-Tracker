from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password= None):
        if not email:
            raise ValueError("Enter email address")
        if not username:
            raise ValueError("Enter username")
        user= self.model(
            email= self.normalize_email(email),
            username= username
        )
        user.set_password(password)
        user.save(using= self.db)
        return user

    def create_superuser(self, email, username, password= None):
        user= self.create_user(
            email= self.normalize_email(email),
            username= username,
            password= password
        )
        user.admin= True
        user.staff= True
        user.superuser= True
        user.save(using= self.db)
        return user
        
class Account(AbstractBaseUser):
    email= models.EmailField(verbose_name= "email", max_length=75, unique= True)
    username= models.CharField(max_length=15, unique= True)
    date_joined= models.DateTimeField(verbose_name= "date joined", auto_now_add= True)
    last_login= models.DateTimeField(verbose_name= "last login date", auto_now= True)
    admin= models.BooleanField(default= False)
    active= models.BooleanField(default= True)
    staff= models.BooleanField(default= False)
    superuser= models.BooleanField(default= False)
    first_name= models.CharField(max_length=25)

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= ['username', 'email', 'first_name']

    objects= MyAccountManager()
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj= None):
        return self.admin
    
    def has_module_perms(self, app_label):
        return True


