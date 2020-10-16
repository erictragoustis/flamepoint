from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

#from https://www.youtube.com/watch?v=eCeRC7E8Z7Y & https://www.youtube.com/watch?v=XJU9vRARkGo&list=PLgCYzUzKIBE_dil025VAJnDjNZHHHR9mW&index=13

class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, telephone, password=None):
        if not username:
            raise ValueError("Users must have an username")
        if not email:
            raise ValueError("Users must have an email")

        user = self.model(
        email = self.normalize_email(email),
        username = username,
        telephone = telephone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, telephone, password):
        user = self.create_user(
        email = self.normalize_email(email),
        password = password,
        username = username,
        telephone = telephone,
        )          

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    first_name = models.CharField(max_length=30)
    telephone= models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS  =['email','telephone']

    objects = MyAccountManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True