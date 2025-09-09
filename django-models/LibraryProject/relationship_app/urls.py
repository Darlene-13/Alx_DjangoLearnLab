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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

