# This if the urls.py file for the relationship_app
from django.urls import path
from relationship_app import views
from relationship_app.views import LibraryDetailView
from django.conf import settings
from django.conf.urls.static import static
from .views import LibraryDetailView, list_books, LoginView, LogoutView, RegisterView

from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/',  LoginView.as_view(template_name='login') , name='login'),
    path('logout/', LogoutView.as_view(template_name='logout'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('admin-dashboard/', views.admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_dashboard'),
    path('member-dashboard/', views.member_view, name='member_dashboard'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

