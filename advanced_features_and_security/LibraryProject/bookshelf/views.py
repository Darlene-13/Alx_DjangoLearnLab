from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model

from .models import Book  # Use relative import for your own models

User = get_user_model()  # Dynamically load your custom user model


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
@permission_required('bookshelf.can_view', login_url='/login/')
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {
        'title': 'View Books',
        'books': books
    })


@permission_required('bookshelf.can_create', login_url='/login/')
def add_book(request):
    # TODO: Add logic to handle form submission
    return render(request, 'bookshelf/add_book.html', {
        'title': 'Add Book'
    })


@permission_required('bookshelf.can_edit', login_url='/login/')
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # TODO: Add logic to handle form submission
    return render(request, 'bookshelf/edit_book.html', {
        'title': 'Edit Book',
        'book': book
    })


@permission_required('bookshelf.can_delete', login_url='/login/')
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # TODO: Add logic to delete book
    return render(request, 'bookshelf/delete_book.html', {
        'title': 'Delete Book',
        'book': book
    })


# ----------------------
# Class-Based Views
# ----------------------
class BookListView(ListView):
    model = Book
    template_name = 'bookshelf/book_list.html'
    context_object_name = 'books'


class CustomUserDetailView(DetailView):
    model = User
    template_name = 'bookshelf/user_detail.html'
    context_object_name = 'custom_user'

    def get_role(self):
        return getattr(self.object, 'role', None)

    def get_date_of_birth(self):
        return getattr(self.object, 'date_of_birth', None)
