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
        user_type,
        **extra_fields
    ):

        user = self.model(
            name=name,
            f_name=f_name,
            phone=phone,
            user_type = user_type
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.user_type = 1
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class users(AbstractBaseUser):
    name = models.CharField(max_length=50, blank=True)
    f_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=32, unique=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    user_type = models.IntegerField()

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name + " " + self.f_name + "(" + self.username + ")"

class Permissions(models.Model):
    pid = models.OneToOneField(users, on_delete=models.CASCADE)
    daily_evaluation = models.BooleanField(default=False)
    personnel = models.BooleanField(default=False)
    overheads = models.BooleanField(default=False)
    groups = models.BooleanField(default=False)
    indicators = models.BooleanField(default=False)
    substitute = models.BooleanField(default=False)
    logs = models.BooleanField(default=False)
    reports = models.BooleanField(default=False)