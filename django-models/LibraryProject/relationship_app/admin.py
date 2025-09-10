from django.contrib import admin
from .models import UserProfile, Author, Book, Library, Librarian

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role')
    list_filter = ('role',)
    ordering = ('user__username',)

admin.site.register(UserProfile, UserProfileAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)
    ordering = ('name',)
admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author__name')
    list_filter = ('author',)
    ordering = ('title',)
admin.site.register(Book, BookAdmin) 

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'books_count')
    search_fields = ('name', 'books__title')
    ordering = ('name',)

    def books_count(self, obj):
        return obj.books.count()
    books_count.short_description = 'Number of Books'

admin.site.register(Library, LibraryAdmin)

class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')
    search_fields = ('name', 'library__name')
    list_filter = ('library',)
    ordering = ('name',)
admin.site.register(Librarian, LibrarianAdmin)