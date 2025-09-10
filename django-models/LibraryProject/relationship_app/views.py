from django.shortcuts import render, redirect
from relationship_app.models import Author, Book, Library, Librarian
from django.contrib.auth import login, logout, authenticate
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect



# Role check functions
def is_admin(user):
    return user.is_authenticated and user.profile.role == 'admin'

def is_librarian(user):
    return user.is_authenticated and user.profile.role == 'librarian'

def is_member(user):
    return user.is_authenticated and user.profile.role == 'member'


# Role-based access control views
@method_decorator(user_passes_test(is_admin, login_url='/login/'), name='dispatch')
class AdminView(TemplateView):
    template_name = 'relationship_app/templates/relationship_app/admin_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Admin Dashboard'
        return context


@method_decorator(user_passes_test(is_librarian, login_url='/login/'), name='dispatch')
class LibrarianView(TemplateView):
    template_name = 'relationship_app/templates/relationship_app/librarian_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Librarian Dashboard'
        return context


@method_decorator(user_passes_test(is_member, login_url='/login/'), name='dispatch')
class MemberView(TemplateView):
    template_name = 'relationship_app/templates/relationship_app/member_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Member Dashboard'
        return context

# Function based views to list all books stored in the database
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
    
# Login view
class LoginView(DetailView):
    template_name = 'relationship_app/logout.html'
    def login_view(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'relationship_app/template/relationship_app/login_success.html', {'title': 'Login Successful'})
            else:
                return render(request, 'relationship_app/template/relationship_app/login.html', {'title': 'Login', 'error': 'Invalid credentials'})
        return render(request, 'relationship_app/template/relationship_app/login.html', {'title': 'Login'})

# Logout view
class LogoutView(DetailView):
    template_name = 'relationship_app/templates/relationship_app/logout.html'

    def logout_view(request):
        logout(request)
        return render(request, 'relationship_app/templates/relationship_app/logout.html', {'title': 'Logout'})

# Register view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Pass POST data to the form
        if form.is_valid():  # Validate input
            user = form.save()  # Create the user in the database
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to home page or another view
    else:
        form = UserCreationForm()  # Empty form for GET request
    
    return render(request, 'relationship_app/register.html', {'form': form})

# Custom check functions
def is_admin(user):
    return user.is_authenticated and user.profile.role == 'admin'

def is_librarian(user):
    return user.is_authenticated and user.profile.role == 'librarian'

def is_member(user):
    return user.is_authenticated and user.profile.role == 'member'


# Permissions

# Add Book
@permission_required('relationship_app.can_add_book', login_url='/login/')
def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return HttpResponse("Book added successfully!")
    return render(request, 'relationship_app/templates/relationship_app/add_book.html')


# Edit Book
@permission_required('relationship_app.can_change_book', login_url='/login/')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return HttpResponse("Book updated successfully!")
    return render(request, 'relationship_app/templates/relationship_app/edit_book.html', {'book': book})


# Delete Book
@permission_required('relationship_app.can_delete_book', login_url='/login/')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return HttpResponse("Book deleted successfully!")
    return render(request, 'relationship_app/templates/relationship_app/delete_book.html', {'book': book})