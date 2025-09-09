# This is a python script that contain sample queries for the relationship_app
from relationship_app.models import Author, Book, Library, Librarian
from django.db.models import Q, Count
from django.utils import timezone

# Query all books for a specific author
def get_books_by_author(author):
    try:
        author = Book.objects.filter(author=author)
        return author.books.all()
    except Author.DoesNotExist:
        return []
    
def get_books_by_author_name(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except Author.DoesNotExist:
        return []

# Query all books in a specific library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []
    
# Query the librarian of a specific library
def get_librarian_of_library(library):
    try:
        library = Library.objects.filter(library=library)
        return library.librarian
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None
    
# Query authors who have written more than a specified number of books
def get_authors_with_min_books(min_books):
    return Author.objects.annotate(book_count=Count('books')).filter(book_count__gt=min_books)
