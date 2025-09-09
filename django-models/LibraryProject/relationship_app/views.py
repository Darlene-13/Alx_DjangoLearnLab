from django.shortcuts import render
from relationship_app.models import Author, Book, Library, Librarian
from django.contrib.auth import login, logout, authenticate
from .models import Library
from django.views.generic.detail import DetailView

# Function based views to list all books stored in the databas
"""View to list all books in the database.
URL: /books/
"""
@staticmethod
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'title': 'List of Books', 'books': books, 'author': Author, 'library': Library, 'librarian': Librarian})

# class based views to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    template_path = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        context['librarian'] = self.object.librarian
        return context
    
