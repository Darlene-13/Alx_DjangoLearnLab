from django.contrib import admin
from .models import CustomUser, Author, Book

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'date_of_birth')
    search_fields = ('username', 'email', 'role')
    list_filter = ('role',)
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)

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