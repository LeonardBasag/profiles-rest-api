from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email adress")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name) #creates a new model that manager represents
        user.set_password(password) # it is encrypted
        user.save(using=self._db) #save the user in django
        return user

    def create_superuser(self, email, name, password):
        """Create and save a super user with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'  # changes the username from Django to mail
    REQUIRED_FIELDS = ['name']  # makes the 'name' field mandatory

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name"""
        return self.name

    def __str__(self):
        """Return string represantation of our user"""
        return self.email
