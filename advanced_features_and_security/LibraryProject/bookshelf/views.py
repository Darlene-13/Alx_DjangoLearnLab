from django.core.exceptions import SuspiciousOperation
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model


from .models import Book  # Relative import for your app models

User = get_user_model()  # Dynamically get the custom user model


# ----------------------
# Role check functions
# ----------------------
def is_admin(user):
    return user.is_authenticated and getattr(user, 'role', None) == 'admin'

def is_librarian(user):
    return user.is_authenticated and getattr(user, 'role', None) == 'librarian'

def is_member(user):
    return user.is_authenticated and getattr(user, 'role', None) == 'member'


# ----------------------
# Permission-based views
# ----------------------
@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    """View all books. Raises PermissionDenied if user lacks permission."""
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {
        'title': 'View Books',
        'books': books
    })


@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    """Add a new book. Raises PermissionDenied if user lacks permission."""
    # TODO: Add form handling logic
    return render(request, 'bookshelf/add_book.html', {
        'title': 'Add Book'
    })


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    """Edit an existing book. Raises PermissionDenied if user lacks permission."""
    book = get_object_or_404(Book, pk=book_id)
    # TODO: Add form handling logic
    return render(request, 'bookshelf/edit_book.html', {
        'title': 'Edit Book',
        'book': book
    })


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    """Delete a book. Raises PermissionDenied if user lacks permission."""
    book = get_object_or_404(Book, pk=book_id)
    # TODO: Add book deletion logic
    return render(request, 'bookshelf/delete_book.html', {
        'title': 'Delete Book',
        'book': book
    })


# ----------------------
# Class-Based Views
# ----------------------
class BookListView(ListView):
    """ListView for all books."""
    model = Book
    template_name = 'bookshelf/book_list.html'
    context_object_name = 'books'


class CustomUserDetailView(DetailView):
    """Detail view for CustomUser."""
    model = User
    template_name = 'bookshelf/user_detail.html'
    context_object_name = 'custom_user'

    def get_role(self):
        return getattr(self.object, 'role', None)

    def get_date_of_birth(self):
        return getattr(self.object, 'date_of_birth', None)


def search_books(request):
    query = request.GET.get('q', '')
    if not query.isalnum():  # Simple input validation
        raise SuspiciousOperation("Invalid search query")

    books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/search_results.html', {'books': books})