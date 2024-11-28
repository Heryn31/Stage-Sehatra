from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """Create and return a regular user with a username, email, and password."""
        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """Create and return a superuser with elevated privileges."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Stored as a hashed password
    created_at = models.DateTimeField(auto_now_add=True)
    is_online = models.BooleanField(default=False)

    # Required fields for authentication
    is_active = models.BooleanField(default=True)  # Is the account active?
    is_staff = models.BooleanField(default=False)  # Can access the admin?

    objects = UserManager()

    USERNAME_FIELD = 'username'  # Used for authentication
    REQUIRED_FIELDS = ['email']  # Required when creating a superuser

    def __str__(self):
        return self.username
