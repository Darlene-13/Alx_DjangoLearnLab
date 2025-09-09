# This if the urls.py file for the relationship_app
from django.urls import path
from relationship_app import views
from relationship_app.views import LibraryDetailView
from django.conf import settings
from django.conf.urls.static import static
from .views import LibraryDetailView, list_books

from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

