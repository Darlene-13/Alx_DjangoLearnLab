from django.contrib import admin
from .models import Book, CustomUser

# Customizing the Admin interface for Book model
class BookAdmin(admin.ModelAdmin):
    # Fields displayed in the list view
    list_display = ("title", "author", "publication_year")

    # Filter sidebar for quick filtering by publication year
    list_filter = ("publication_year",)

    # Search functionality by title and author
    search_fields = ("title", "author")
admin.site.register(Book, BookAdmin)

   
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'date_of_birth')
    search_fields = ('username', 'email', 'role')
    list_filter = ('role',)
    ordering = ('username',)
admin.site.register(CustomUser, CustomUserAdmin)

