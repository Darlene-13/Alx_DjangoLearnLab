from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('member', 'Member'),
        ('librarian', 'Librarian'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member', help_text="Select the user role")
    date_of_birth = models.DateField(null=True, blank=True, help_text="Enter the user's date of birth")
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True, help_text="Upload a profile photo")

    def __str__(self):
        return f"{self.username} - {self.role}"
    
    class Meta:
        db_table = "custom_user"
        ordering = ['username']
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

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

class Author(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the author's name")
    birth_date = models.DateField(help_text="Enter the author's birth date")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "relationship_app_author"
        ordering = ['name']
        verbose_name = "Author"
        verbose_name_plural = "Authors"

class Book(models.Model):
    title = models.CharField(max_length = 200, help_text="Enter the book title")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', help_text="Select the author of the book")
    publication_year = models.IntegerField(help_text="Enter the publication year")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "relationship_app_book"
        ordering = ['title']
        verbose_name = "Book"
        verbose_name_plural = "Books"
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
            ("can_view_book", "Can view book"),
        ]



class Library(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the library name")
    books = models.ManyToManyField(Book, related_name='libraries', help_text="Select books available in the library")

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "relationship_app_library"
        ordering = ['name']
        verbose_name = "Library"
        verbose_name_plural = "Libraries"

class Librarian(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the librarian's name")
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian', help_text="Select the library the librarian works at")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "relationship_app_librarian"
        ordering = ['name']
        verbose_name = "Librarian"
        verbose_name_plural = "Librarians"

