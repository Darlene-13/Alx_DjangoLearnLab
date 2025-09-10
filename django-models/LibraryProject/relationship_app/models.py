from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile', help_text="Link to the custom user profile")
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('member', 'Member'),
        ('librarian', 'Librarian'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member', help_text="Select the user role")

    def __str__(self):
        return f"{self.user.username} - {self.role}"

    class Meta:
        db_table = "relationship_app_userprofile"
        ordering = ['user__username']
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"



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

