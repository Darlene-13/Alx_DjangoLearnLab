from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the book title")
    author = models.CharField(max_length=100, help_text="Enter the author's name")
    publication_year = models.IntegerField(help_text="Enter the publication year")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "bookshelf_book"
        ordering = ['title']
        verbose_name = "Book"
        verbose_name_plural = "Books"

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('member', 'Member'),
        ('librarian', 'Librarian'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member', help_text="Select the user role")
    date_of_birth = models.DateField(null=True, blank=True, help_text="Enter the user's date of birth")
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True, help_text="Upload a profile photo")

    objects = UserManager()

    def __str__(self):
        return f"{self.username} - {self.role}"

    class Meta:
        db_table = "bookshelf_customuser"
        ordering = ['username']
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

class CustomUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)