from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# import Abs
# AbstractUsers
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(
        self,
        name,
        f_name,
        phone,
        password,
        **extra_fields
    ):

        user = self.model(
            name=name,
            f_name=f_name,
            phone=phone,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class users(AbstractBaseUser):
    name = models.CharField(max_length=50, blank=True)
    f_name = models.CharField(max_length=50, blank=True)
    username = models.IntegerField(unique=True)

    def clean(self):
        if not isinstance(self.username, int):
            raise ValueError("Username should be an integer")

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name + " " + self.f_name + "(" + str(self.username) + ")"
    
    def __repr__(self) -> str:
        return self.username

class Permissions(models.Model):
    pid = models.OneToOneField(users, on_delete=models.CASCADE)
    daily_evaluation = models.BooleanField(default=True,)
    personnel = models.BooleanField(default=True)
    overheads = models.BooleanField(default=True)
    groups = models.BooleanField(default=True)
    indicators = models.BooleanField(default=True)
    substitute = models.BooleanField(default=True)
    logs = models.BooleanField(default=True)
    logs = models.BooleanField(default=True)
    reports = models.BooleanField(default=True)