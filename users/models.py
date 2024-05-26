from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# import Abs
# AbstractUsers
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, name, f_name, phone, password, email, inv_code, date_of_birth, expiration, **extra_fields):
        if not email:
            raise ValueError("email is required")
        
        user = self.model(
            name = name,
            f_name = f_name,
            phone = phone,
            email = self.normalize_email(email),
            inv_code = inv_code,
            date_of_birth = date_of_birth,
            expiration = expiration,
            **extra_fields
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, username, password, **extra_fields):
        user = self.model(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class users(AbstractBaseUser):
    name = models.CharField(max_length=50, blank=True)
    f_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=32, unique=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    email = models.CharField(max_length=320, unique=True, null=True, blank=True)
    inv_code = models.CharField(max_length=17, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_of_birth = models.CharField(max_length=20, null=True, blank=True)
    expiration = models.CharField(max_length=3, blank=True, default="30")
    orcid = models.CharField(max_length=2048, null=True, blank=True, default=None)
    g_scholar = models.CharField(max_length=2048, null=True, blank=True, default=None)
    g_patent = models.CharField(max_length=2048, null=True, blank=True, default=None)
    image = models.ImageField(upload_to='static/')

    objects = UserManager()
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name + " " +self.f_name + "(" + self.username + ")"