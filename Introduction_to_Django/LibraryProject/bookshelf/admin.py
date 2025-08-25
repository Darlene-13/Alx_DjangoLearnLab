from django.contrib import admin
from .models import Book

# Customizing the Admin interface for Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields displayed in the list view
    list_display = ("title", "author", "publication_year")

    # Filter sidebar for quick filtering by publication year
    list_filter = ("publication_year",)

    # Search functionality by title and author
    search_fields = ("title", "author")

    # Optional
