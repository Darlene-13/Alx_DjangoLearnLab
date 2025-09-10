from django.shortcuts import render, redirect
from relationship_app.models import Author, Book, Library, Librarian
from django.contrib.auth import login, logout, authenticate
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

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

# Admin view
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return HttpResponse("Admin Dashboard")

# Librarian view
@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return HttpResponse("Librarian Dashboard")

# Member view
@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return HttpResponse("Member Dashboard")