from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# from matplotlib.pyplot import cla
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self,name, email, password=None):
        """create new user profile"""
        if not email:
            raise ValueError('please enter a valid email')
        email = self.normalize_email(email)
        user = self.model(email=email, name =name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self, email, name, password):
        """create and save new user with details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """"full name of user"""
        return self.name
    
    def get_short_name(self):
        """short name of user"""
        return self.name
    def __str__(self):
        """return string representation of the user"""
        return self.email
